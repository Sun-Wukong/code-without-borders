"""
NYC Benefits Screening Tool for CrewAI

This tool provides a unified interface to the NYC Benefits Screening API,
handling authentication and eligibility screening in a single tool.
"""

import os
import sys
from typing import Type, Optional, Dict, Any, List
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

# Add the ny_benefits_oas package to the path
ny_benefits_oas_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
    'ny_benefits_oas'
)
if ny_benefits_oas_path not in sys.path:
    sys.path.insert(0, ny_benefits_oas_path)

try:
    from openapi_client import ApiClient, Configuration, DefaultApi
    from openapi_client.models import (
        Credentials, Submission, Household, Person, 
        Income, Expense
    )
    from openapi_client.rest import ApiException
except ImportError as e:
    raise ImportError(
        f"Failed to import openapi_client. Make sure ny_benefits_oas is installed. Error: {e}"
    )


class BenefitsScreeningInput(BaseModel):
    """Input schema for NYC Benefits Screening Tool."""
    
    # Household Information
    cash_on_hand: int = Field(
        default=0,
        description="Total cash on hand, checking/savings accounts, stocks, bonds, or mutual funds (in dollars)",
        ge=0
    )
    living_situation: str = Field(
        default="renting",
        description="Current living situation: 'renting', 'owner', 'staying_with_friend', 'hotel', 'shelter', or 'prefer_not_to_say'"
    )
    housing_rental_type: Optional[str] = Field(
        default=None,
        description="If renting, specify type: 'MarketRate', 'RentControlled', 'FamilyHome', 'Condo', 'NYCHA', 'RentRegulatedHotel', 'Section213', 'LimitedDividendDevelopment', 'MitchellLama', 'RedevelopmentCompany', or 'HDFC'"
    )
    
    # Person Information (simplified - can be extended)
    age: int = Field(
        description="Age of the person being screened",
        ge=0,
        le=120
    )
    has_income: bool = Field(
        default=False,
        description="Whether the person has any income"
    )
    monthly_income: int = Field(
        default=0,
        description="Total monthly income in dollars",
        ge=0
    )
    income_type: Optional[str] = Field(
        default=None,
        description="Type of income: 'wages', 'selfEmployment', 'unemployment', 'cashAssistance', 'childSupport', 'disability', 'socialSecurity', 'veteransBenefits', 'pension', 'deferredComp', 'workersComp', 'alimony', 'boarder', 'interest', 'rental', 'other'"
    )
    
    has_expenses: bool = Field(
        default=False,
        description="Whether the person has expenses"
    )
    monthly_rent: int = Field(
        default=0,
        description="Monthly rent payment in dollars",
        ge=0
    )
    
    # Optional filters
    interested_programs: Optional[str] = Field(
        default=None,
        description="Pipe-separated list of program codes to filter results (e.g., 'SNAP|CASH_ASSISTANCE|WIC'). Leave empty to check all programs."
    )
    
    # API Configuration (optional - will use env vars if not provided)
    api_host: Optional[str] = Field(
        default=None,
        description="NYC Benefits API host URL (defaults to env var NYC_BENEFITS_API_HOST or production URL)"
    )
    username: Optional[str] = Field(
        default=None,
        description="API username (defaults to env var NYC_BENEFITS_USERNAME)"
    )
    password: Optional[str] = Field(
        default=None,
        description="API password (defaults to env var NYC_BENEFITS_PASSWORD)"
    )


class NYCBenefitsScreeningTool(BaseTool):
    """
    NYC Benefits Screening Tool
    
    This tool screens individuals and households for eligibility in NYC benefit programs.
    It handles authentication automatically and returns a list of programs the household
    may be eligible for based on the provided information.
    
    The tool uses the NYC Benefits Screening API and requires valid credentials.
    Credentials can be provided directly or via environment variables:
    - NYC_BENEFITS_API_HOST (default: https://screeningapi.cityofnewyork.us)
    - NYC_BENEFITS_USERNAME
    - NYC_BENEFITS_PASSWORD
    """
    
    name: str = "nyc_benefits_screening"
    description: str = (
        "Screens individuals and households for eligibility in NYC benefit programs. "
        "Provide household information (cash on hand, living situation), person details "
        "(age, income, expenses), and optionally filter by specific programs. "
        "Returns a list of eligible benefit programs with details about each program."
    )
    args_schema: Type[BaseModel] = BenefitsScreeningInput
    
    # Cache for authentication token
    _auth_token: Optional[str] = None
    _api_config: Optional[Configuration] = None
    
    def _get_api_config(
        self, 
        api_host: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None
    ) -> Configuration:
        """Get or create API configuration."""
        if self._api_config is None:
            config = Configuration()
            config.host = api_host or os.getenv(
                'NYC_BENEFITS_API_HOST', 
                'https://screeningapi.cityofnewyork.us'
            )
            self._api_config = config
        return self._api_config
    
    def _authenticate(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        api_host: Optional[str] = None
    ) -> str:
        """
        Authenticate with the NYC Benefits API and return auth token.
        Uses cached token if available.
        """
        # Return cached token if available
        if self._auth_token:
            return self._auth_token
        
        # Get credentials from parameters or environment
        api_username = username or os.getenv('NYC_BENEFITS_USERNAME')
        api_password = password or os.getenv('NYC_BENEFITS_PASSWORD')
        
        if not api_username or not api_password:
            raise ValueError(
                "API credentials not provided. Set NYC_BENEFITS_USERNAME and "
                "NYC_BENEFITS_PASSWORD environment variables or pass them as parameters."
            )
        
        try:
            config = self._get_api_config(api_host)
            
            with ApiClient(config) as api_client:
                api = DefaultApi(api_client)
                credentials = Credentials(
                    username=api_username,
                    password=api_password
                )
                
                token_response = api.authenticate(credentials=credentials)
                self._auth_token = token_response.token
                return self._auth_token
                
        except ApiException as e:
            raise Exception(f"Authentication failed: {e.status} - {e.reason}")
        except Exception as e:
            raise Exception(f"Authentication error: {str(e)}")
    
    def _create_household(
        self,
        cash_on_hand: int,
        living_situation: str,
        housing_rental_type: Optional[str]
    ) -> Household:
        """Create a Household object from input parameters."""
        living_map = {
            'renting': {'living_renting': True},
            'owner': {'living_owner': True},
            'staying_with_friend': {'living_staying_with_friend': True},
            'hotel': {'living_hotel': True},
            'shelter': {'living_shelter': True},
            'prefer_not_to_say': {'living_prefer_not_to_say': True}
        }
        
        living_params = living_map.get(living_situation.lower(), {'living_renting': True})
        
        household_data = {
            'cash_on_hand': cash_on_hand,
            'housing_rental_type': housing_rental_type or '',
            **living_params
        }
        
        return Household(**household_data)
    
    def _create_person(
        self,
        age: int,
        has_income: bool,
        monthly_income: int,
        income_type: Optional[str],
        has_expenses: bool,
        monthly_rent: int
    ) -> Person:
        """Create a Person object from input parameters."""
        person_data: Dict[str, Any] = {
            'age': age,
        }
        
        # Add income if specified
        incomes: List[Income] = []
        if has_income and monthly_income > 0:
            income_data = {
                'amount': monthly_income,
                'type': income_type or 'wages'
            }
            incomes.append(Income(**income_data))
        
        if incomes:
            person_data['incomes'] = incomes
        
        # Add expenses if specified
        expenses: List[Expense] = []
        if has_expenses and monthly_rent > 0:
            expense_data = {
                'amount': monthly_rent,
                'type': 'rent'
            }
            expenses.append(Expense(**expense_data))
        
        if expenses:
            person_data['expenses'] = expenses
        
        return Person(**person_data)
    
    def _run(
        self,
        cash_on_hand: int = 0,
        living_situation: str = "renting",
        housing_rental_type: Optional[str] = None,
        age: int = 0,
        has_income: bool = False,
        monthly_income: int = 0,
        income_type: Optional[str] = None,
        has_expenses: bool = False,
        monthly_rent: int = 0,
        interested_programs: Optional[str] = None,
        api_host: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None
    ) -> str:
        """
        Execute the benefits screening.
        
        Returns a formatted string with eligible programs and their details.
        """
        try:
            # Step 1: Authenticate
            auth_token = self._authenticate(username, password, api_host)
            
            # Step 2: Create household and person objects
            household = self._create_household(
                cash_on_hand, living_situation, housing_rental_type
            )
            person = self._create_person(
                age, has_income, monthly_income, income_type, 
                has_expenses, monthly_rent
            )
            
            # Step 3: Create submission
            submission = Submission(
                household=[household],
                person=[person]
            )
            
            # Step 4: Call the screening API
            config = self._get_api_config(api_host)
            config.access_token = auth_token
            
            with ApiClient(config) as api_client:
                api = DefaultApi(api_client)
                
                response = api.get_eligible_programs(
                    submission=submission,
                    interested_programs=interested_programs
                )
                
                # Step 5: Format the response
                if not response.eligible_programs:
                    return "No eligible programs found based on the provided information."
                
                result_lines = [
                    f"Found {len(response.eligible_programs)} eligible program(s):\n"
                ]
                
                for idx, program in enumerate(response.eligible_programs, 1):
                    result_lines.append(f"\n{idx}. {program.name}")
                    if program.external_name:
                        result_lines.append(f"   External Name: {program.external_name}")
                    if program.guid:
                        result_lines.append(f"   Program ID: {program.guid}")
                    if hasattr(program, 'description') and program.description:
                        result_lines.append(f"   Description: {program.description}")
                
                return "\n".join(result_lines)
                
        except ApiException as e:
            return f"API Error: {e.status} - {e.reason}\nDetails: {e.body if hasattr(e, 'body') else 'No additional details'}"
        except ValueError as e:
            return f"Configuration Error: {str(e)}"
        except Exception as e:
            return f"Error during screening: {str(e)}"


# Convenience function to create the tool
def create_nyc_benefits_screening_tool() -> NYCBenefitsScreeningTool:
    """
    Factory function to create an instance of the NYC Benefits Screening Tool.
    
    Returns:
        NYCBenefitsScreeningTool: Configured tool instance
    """
    return NYCBenefitsScreeningTool()

# Made with Bob
