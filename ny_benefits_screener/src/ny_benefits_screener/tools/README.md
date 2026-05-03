# NYC Benefits Screening Tool for CrewAI

A custom CrewAI tool that integrates with the NYC Benefits Screening API to check eligibility for NYC benefit programs.

## Overview

The `NYCBenefitsScreeningTool` is a unified tool that handles both authentication and benefits screening in a single interface. It's designed to be used by CrewAI agents to help individuals and families discover NYC benefit programs they may be eligible for.

## Features

- ✅ **Automatic Authentication**: Handles API authentication internally with token caching
- ✅ **Simplified Interface**: Single tool for complete screening workflow
- ✅ **Type-Safe Inputs**: Uses Pydantic models for input validation
- ✅ **Flexible Configuration**: Supports environment variables or direct parameter passing
- ✅ **Error Handling**: Comprehensive error handling with clear messages
- ✅ **Program Filtering**: Optional filtering by specific program codes

## Installation

### Prerequisites

1. **Install the NYC Benefits OpenAPI Client**:
   ```bash
   cd ny_benefits_oas
   pip install -e .
   ```

2. **Install CrewAI** (if not already installed):
   ```bash
   pip install crewai crewai-tools
   ```

3. **Set up environment variables** (recommended):
   ```bash
   export NYC_BENEFITS_API_HOST="https://screeningapi.cityofnewyork.us"
   export NYC_BENEFITS_USERNAME="your_username"
   export NYC_BENEFITS_PASSWORD="your_password"
   ```

   Or create a `.env` file in your project root:
   ```env
   NYC_BENEFITS_API_HOST=https://screeningapi.cityofnewyork.us
   NYC_BENEFITS_USERNAME=your_username
   NYC_BENEFITS_PASSWORD=your_password
   ```

## Usage

### Basic Usage in CrewAI

```python
from crewai import Agent, Task, Crew
from ny_benefits_screener.tools import NYCBenefitsScreeningTool

# Create the tool
screening_tool = NYCBenefitsScreeningTool()

# Create an agent with the tool
benefits_counselor = Agent(
    role="NYC Benefits Counselor",
    goal="Help New Yorkers find benefit programs they're eligible for",
    backstory="You are an expert in NYC social services and benefit programs. "
              "You help families and individuals navigate the complex landscape "
              "of available assistance programs.",
    tools=[screening_tool],
    verbose=True
)

# Create a task
screening_task = Task(
    description="""
    Screen a 35-year-old person who:
    - Lives in a rented apartment (market rate)
    - Has $500 in cash on hand
    - Earns $2,000 per month from wages
    - Pays $1,200 per month in rent
    
    Find all NYC benefit programs they may be eligible for.
    """,
    agent=benefits_counselor,
    expected_output="A list of eligible NYC benefit programs with descriptions"
)

# Create and run the crew
crew = Crew(
    agents=[benefits_counselor],
    tasks=[screening_task],
    verbose=True
)

result = crew.kickoff()
print(result)
```

### Direct Tool Usage (for testing)

```python
from ny_benefits_screener.tools import create_nyc_benefits_screening_tool

# Create tool instance
tool = create_nyc_benefits_screening_tool()

# Run screening
result = tool._run(
    age=35,
    cash_on_hand=500,
    living_situation="renting",
    housing_rental_type="MarketRate",
    has_income=True,
    monthly_income=2000,
    income_type="wages",
    has_expenses=True,
    monthly_rent=1200
)

print(result)
```

## Input Parameters

### Household Information

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cash_on_hand` | int | No | Total cash, savings, stocks, bonds (in dollars). Default: 0 |
| `living_situation` | str | No | One of: 'renting', 'owner', 'staying_with_friend', 'hotel', 'shelter', 'prefer_not_to_say'. Default: 'renting' |
| `housing_rental_type` | str | No | If renting, specify type: 'MarketRate', 'RentControlled', 'NYCHA', etc. |

### Person Information

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `age` | int | Yes | Age of the person (0-120) |
| `has_income` | bool | No | Whether person has income. Default: False |
| `monthly_income` | int | No | Monthly income in dollars. Default: 0 |
| `income_type` | str | No | Type: 'wages', 'selfEmployment', 'unemployment', 'socialSecurity', etc. |
| `has_expenses` | bool | No | Whether person has expenses. Default: False |
| `monthly_rent` | int | No | Monthly rent payment in dollars. Default: 0 |

### Optional Filters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `interested_programs` | str | No | Pipe-separated program codes (e.g., 'SNAP\|WIC\|CASH_ASSISTANCE') |

### API Configuration (Optional)

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_host` | str | No | API host URL (uses env var if not provided) |
| `username` | str | No | API username (uses env var if not provided) |
| `password` | str | No | API password (uses env var if not provided) |

## Living Situation Options

- **renting**: Currently renting an apartment or house
- **owner**: Owns the home or apartment
- **staying_with_friend**: Temporarily staying with friends/family
- **hotel**: Living in a hotel
- **shelter**: In a shelter or experiencing homelessness
- **prefer_not_to_say**: Prefer not to disclose

## Housing Rental Types (if renting)

- **MarketRate**: Market rate rental
- **RentControlled**: Rent controlled apartment
- **FamilyHome**: Family home
- **Condo**: Condominium
- **NYCHA**: NYC Housing Authority
- **RentRegulatedHotel**: Rent regulated hotel
- **Section213**: Section 213 housing
- **LimitedDividendDevelopment**: Limited dividend development
- **MitchellLama**: Mitchell-Lama housing
- **RedevelopmentCompany**: Redevelopment company housing
- **HDFC**: Housing Development Fund Corporation

## Income Types

- **wages**: Employment wages
- **selfEmployment**: Self-employment income
- **unemployment**: Unemployment benefits
- **cashAssistance**: Cash assistance
- **childSupport**: Child support payments
- **disability**: Disability benefits
- **socialSecurity**: Social Security benefits
- **veteransBenefits**: Veterans benefits
- **pension**: Pension income
- **deferredComp**: Deferred compensation
- **workersComp**: Workers compensation
- **alimony**: Alimony payments
- **boarder**: Boarder income
- **interest**: Interest income
- **rental**: Rental income
- **other**: Other income sources

## Output Format

The tool returns a formatted string containing:
- Number of eligible programs found
- For each program:
  - Program name
  - External name (if available)
  - Program ID (GUID)
  - Description (if available)

Example output:
```
Found 3 eligible program(s):

1. Supplemental Nutrition Assistance Program (SNAP)
   External Name: Food Stamps
   Program ID: abc-123-def
   Description: Helps low-income individuals and families buy food

2. Emergency Rental Assistance Program
   External Name: ERAP
   Program ID: xyz-789-ghi
   Description: Provides rental assistance to eligible households

3. Home Energy Assistance Program
   External Name: HEAP
   Program ID: mno-456-pqr
   Description: Helps with heating and cooling costs
```

## Error Handling

The tool handles various error scenarios:

- **Missing Credentials**: Returns clear error message if credentials not provided
- **Authentication Failures**: Reports API authentication errors
- **API Errors**: Provides detailed error information from the API
- **Invalid Input**: Validates input parameters using Pydantic

## Advanced Usage

### Filtering by Specific Programs

```python
result = tool._run(
    age=30,
    cash_on_hand=1000,
    living_situation="renting",
    has_income=True,
    monthly_income=1500,
    # Only check for SNAP and WIC
    interested_programs="SNAP|WIC"
)
```

### Using Custom API Credentials

```python
result = tool._run(
    age=40,
    cash_on_hand=200,
    living_situation="shelter",
    # Provide credentials directly
    api_host="https://api.example.com",
    username="custom_user",
    password="custom_pass"
)
```

## Troubleshooting

### Import Errors

If you see import errors for `openapi_client`:
```bash
cd ny_benefits_oas
pip install -e .
```

### Authentication Errors

1. Verify your credentials are correct
2. Check that environment variables are set properly
3. Ensure the API host URL is correct
4. Verify your account has API access

### No Programs Found

This is normal if the person doesn't meet eligibility criteria for any programs. Try:
- Adjusting income levels
- Changing living situation
- Modifying household composition

## Contributing

To extend the tool:

1. **Add more person/household fields**: Update `BenefitsScreeningInput` and the `_create_person`/`_create_household` methods
2. **Support multiple household members**: Modify to accept lists of persons
3. **Add result caching**: Implement caching for repeated queries
4. **Enhanced formatting**: Customize the output format in the `_run` method

## API Documentation

For more information about the NYC Benefits Screening API:
- API Documentation: Check the `ny_benefits_oas/docs/` directory
- OpenAPI Spec: `nyc-benefits-screening-api.yml`

## License

This tool is part of the NYC Benefits Screener project. See the main project LICENSE file for details.