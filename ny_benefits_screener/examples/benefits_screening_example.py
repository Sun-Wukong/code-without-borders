"""
Example: Using NYC Benefits Screening Tool with CrewAI

This example demonstrates how to use the NYCBenefitsScreeningTool
in a CrewAI workflow to help individuals find eligible benefit programs.
"""

import os
from crewai import Agent, Task, Crew, Process
from ny_benefits_screener.tools import NYCBenefitsScreeningTool

# Ensure environment variables are set
# You can also set these in a .env file
# os.environ['NYC_BENEFITS_API_HOST'] = 'https://screeningapi.cityofnewyork.us'
# os.environ['NYC_BENEFITS_USERNAME'] = 'your_username'
# os.environ['NYC_BENEFITS_PASSWORD'] = 'your_password'


def example_1_basic_screening():
    """
    Example 1: Basic benefits screening for a single individual
    """
    print("\n" + "="*60)
    print("Example 1: Basic Benefits Screening")
    print("="*60 + "\n")
    
    # Create the screening tool
    screening_tool = NYCBenefitsScreeningTool()
    
    # Create a benefits counselor agent
    benefits_counselor = Agent(
        role="NYC Benefits Counselor",
        goal="Help New Yorkers discover benefit programs they're eligible for",
        backstory="""You are an experienced social worker specializing in NYC 
        benefit programs. You have deep knowledge of eligibility requirements 
        and help people navigate the application process.""",
        tools=[screening_tool],
        verbose=True
    )
    
    # Create a screening task
    screening_task = Task(
        description="""
        Screen a 28-year-old individual with the following situation:
        - Living in a rented apartment (market rate)
        - Has $300 in cash savings
        - Works part-time earning $1,500 per month
        - Pays $1,000 per month in rent
        
        Find all NYC benefit programs they may be eligible for and 
        provide a summary of each program.
        """,
        agent=benefits_counselor,
        expected_output="""A comprehensive list of eligible benefit programs 
        with brief descriptions of what each program offers."""
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[benefits_counselor],
        tasks=[screening_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    return result


def example_2_family_screening():
    """
    Example 2: Screening for a family with multiple considerations
    """
    print("\n" + "="*60)
    print("Example 2: Family Benefits Screening")
    print("="*60 + "\n")
    
    screening_tool = NYCBenefitsScreeningTool()
    
    # Create a family benefits specialist
    family_specialist = Agent(
        role="Family Benefits Specialist",
        goal="Help families maximize their benefit eligibility",
        backstory="""You specialize in helping families with children 
        navigate NYC's social services. You understand the unique challenges 
        families face and know how to identify all available support programs.""",
        tools=[screening_tool],
        verbose=True
    )
    
    # Create a task for a family scenario
    family_task = Task(
        description="""
        Screen for a family with the following situation:
        - Parent is 35 years old
        - Living in NYCHA housing (public housing)
        - Has $150 in cash on hand
        - Receives $800 per month in unemployment benefits
        - Pays $400 per month in rent (subsidized)
        
        Identify all benefit programs this family might qualify for,
        especially those that help with food, childcare, and utilities.
        """,
        agent=family_specialist,
        expected_output="""A detailed report of eligible programs with 
        emphasis on family-focused benefits like SNAP, WIC, and childcare assistance."""
    )
    
    crew = Crew(
        agents=[family_specialist],
        tasks=[family_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    return result


def example_3_senior_screening():
    """
    Example 3: Benefits screening for a senior citizen
    """
    print("\n" + "="*60)
    print("Example 3: Senior Citizen Benefits Screening")
    print("="*60 + "\n")
    
    screening_tool = NYCBenefitsScreeningTool()
    
    # Create a senior services specialist
    senior_specialist = Agent(
        role="Senior Services Specialist",
        goal="Help senior citizens access all available benefits and services",
        backstory="""You are an expert in programs for older adults in NYC. 
        You understand Medicare, Social Security, SCRIE, and other senior-specific 
        programs. You help seniors maintain their independence and quality of life.""",
        tools=[screening_tool],
        verbose=True
    )
    
    # Create a task for a senior scenario
    senior_task = Task(
        description="""
        Screen for a 72-year-old senior with the following situation:
        - Lives in a rent-controlled apartment
        - Has $2,000 in savings
        - Receives $1,200 per month in Social Security
        - Pays $800 per month in rent
        
        Find all benefit programs available, with special attention to 
        programs that help with rent, utilities, and healthcare costs.
        """,
        agent=senior_specialist,
        expected_output="""A comprehensive list of senior-focused benefit 
        programs including rent assistance, utility help, and food programs."""
    )
    
    crew = Crew(
        agents=[senior_specialist],
        tasks=[senior_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    return result


def example_4_multi_agent_consultation():
    """
    Example 4: Multi-agent collaboration for comprehensive benefit analysis
    """
    print("\n" + "="*60)
    print("Example 4: Multi-Agent Benefits Consultation")
    print("="*60 + "\n")
    
    screening_tool = NYCBenefitsScreeningTool()
    
    # Create multiple specialized agents
    screener = Agent(
        role="Benefits Screener",
        goal="Accurately screen individuals for benefit eligibility",
        backstory="""You are a technical specialist who runs benefit 
        eligibility screenings and provides raw data about eligible programs.""",
        tools=[screening_tool],
        verbose=True
    )
    
    advisor = Agent(
        role="Benefits Advisor",
        goal="Provide personalized advice on benefit programs",
        backstory="""You are a counselor who interprets screening results 
        and provides actionable advice on which programs to apply for first 
        and how to maximize benefits.""",
        verbose=True
    )
    
    # Create tasks
    screening_task = Task(
        description="""
        Screen a 45-year-old individual:
        - Living in a shelter (experiencing homelessness)
        - Has $50 in cash
        - No current income
        - No rent expenses (in shelter)
        
        Run a complete benefits screening.
        """,
        agent=screener,
        expected_output="Complete list of all eligible benefit programs"
    )
    
    advisory_task = Task(
        description="""
        Based on the screening results, provide a prioritized action plan:
        1. Which programs to apply for immediately
        2. Which programs provide the most critical support
        3. Any programs that work well together
        4. Next steps for the individual
        """,
        agent=advisor,
        expected_output="""A prioritized action plan with specific 
        recommendations and next steps""",
        context=[screening_task]  # This task depends on screening_task
    )
    
    # Create crew with sequential process
    crew = Crew(
        agents=[screener, advisor],
        tasks=[screening_task, advisory_task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    return result


def example_5_filtered_screening():
    """
    Example 5: Screening with program filters
    """
    print("\n" + "="*60)
    print("Example 5: Filtered Benefits Screening")
    print("="*60 + "\n")
    
    screening_tool = NYCBenefitsScreeningTool()
    
    specialist = Agent(
        role="Food Assistance Specialist",
        goal="Help people access food assistance programs",
        backstory="""You specialize in food security programs like SNAP, 
        WIC, and emergency food assistance. You help people understand 
        their options for getting nutritious food.""",
        tools=[screening_tool],
        verbose=True
    )
    
    task = Task(
        description="""
        Screen a 30-year-old individual for FOOD-RELATED programs only:
        - Living with friends temporarily
        - Has $100 in cash
        - Earns $1,000 per month from part-time work
        - No rent expenses currently
        
        Focus specifically on SNAP and other food assistance programs.
        Use the interested_programs filter to check only food-related programs.
        """,
        agent=specialist,
        expected_output="List of food assistance programs the person qualifies for"
    )
    
    crew = Crew(
        agents=[specialist],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff()
    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)
    print(result)
    return result


def main():
    """
    Run all examples
    """
    print("\n" + "="*60)
    print("NYC BENEFITS SCREENING TOOL - CREWAI EXAMPLES")
    print("="*60)
    
    # Check if credentials are set
    if not all([
        os.getenv('NYC_BENEFITS_USERNAME'),
        os.getenv('NYC_BENEFITS_PASSWORD')
    ]):
        print("\n⚠️  WARNING: API credentials not found in environment variables!")
        print("Please set the following environment variables:")
        print("  - NYC_BENEFITS_API_HOST (optional, defaults to production)")
        print("  - NYC_BENEFITS_USERNAME (required)")
        print("  - NYC_BENEFITS_PASSWORD (required)")
        print("\nYou can set them in a .env file or export them in your shell.")
        return
    
    # Run examples (comment out any you don't want to run)
    try:
        example_1_basic_screening()
        # example_2_family_screening()
        # example_3_senior_screening()
        # example_4_multi_agent_consultation()
        # example_5_filtered_screening()
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("\nMake sure:")
        print("1. The ny_benefits_oas package is installed")
        print("2. Your API credentials are correct")
        print("3. You have network access to the API")


if __name__ == "__main__":
    main()

# Made with Bob
