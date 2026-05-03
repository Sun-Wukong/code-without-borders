# NYC Benefits Screener - Setup Guide

Quick setup guide for using the NYC Benefits Screening Tool with CrewAI.

## Prerequisites

- Python 3.9 or higher
- pip or uv package manager
- NYC Benefits API credentials (username and password)

## Installation Steps

### 1. Install the NYC Benefits OpenAPI Client

```bash
cd ny_benefits_oas
pip install -e .
```

Or with uv:
```bash
cd ny_benefits_oas
uv pip install -e .
```

### 2. Install CrewAI

```bash
pip install crewai crewai-tools
```

Or with uv:
```bash
uv pip install crewai crewai-tools
```

### 3. Install Additional Dependencies

```bash
pip install pydantic python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the `ny_benefits_screener` directory:

```env
# NYC Benefits API Configuration
NYC_BENEFITS_API_HOST=https://screeningapi.cityofnewyork.us
NYC_BENEFITS_USERNAME=your_username_here
NYC_BENEFITS_PASSWORD=your_password_here
```

**Important**: Add `.env` to your `.gitignore` to keep credentials secure!

Alternatively, export environment variables in your shell:

```bash
export NYC_BENEFITS_API_HOST="https://screeningapi.cityofnewyork.us"
export NYC_BENEFITS_USERNAME="your_username"
export NYC_BENEFITS_PASSWORD="your_password"
```

## Verify Installation

Test that everything is installed correctly:

```python
# test_installation.py
from ny_benefits_screener.tools import NYCBenefitsScreeningTool

# Create tool instance
tool = NYCBenefitsScreeningTool()
print("✅ Tool created successfully!")

# Test basic functionality (requires valid credentials)
try:
    result = tool._run(
        age=30,
        cash_on_hand=500,
        living_situation="renting",
        has_income=True,
        monthly_income=2000
    )
    print("✅ Tool execution successful!")
    print(result)
except Exception as e:
    print(f"❌ Error: {e}")
```

Run the test:
```bash
python test_installation.py
```

## Quick Start

### Basic Usage

```python
from crewai import Agent, Task, Crew
from ny_benefits_screener.tools import NYCBenefitsScreeningTool

# Create the tool
screening_tool = NYCBenefitsScreeningTool()

# Create an agent
agent = Agent(
    role="Benefits Counselor",
    goal="Help people find eligible NYC benefits",
    backstory="Expert in NYC social services",
    tools=[screening_tool],
    verbose=True
)

# Create a task
task = Task(
    description="Screen a 35-year-old with $500 savings, earning $2000/month",
    agent=agent,
    expected_output="List of eligible programs"
)

# Run
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
print(result)
```

## Project Structure

After setup, your project should look like this:

```
code-without-borders/
├── ny_benefits_oas/              # OpenAPI client package
│   ├── openapi_client/
│   ├── setup.py
│   └── ...
├── ny_benefits_screener/         # CrewAI project
│   ├── src/
│   │   └── ny_benefits_screener/
│   │       └── tools/
│   │           ├── __init__.py
│   │           ├── nyc_benefits_screening_tool.py
│   │           └── README.md
│   ├── examples/
│   │   └── benefits_screening_example.py
│   ├── .env                      # Your credentials (gitignored)
│   └── SETUP_GUIDE.md           # This file
└── ...
```

## Running Examples

The `examples/` directory contains several usage examples:

```bash
cd ny_benefits_screener
python examples/benefits_screening_example.py
```

Examples include:
1. Basic screening for an individual
2. Family benefits screening
3. Senior citizen screening
4. Multi-agent collaboration
5. Filtered screening (specific programs)

## Troubleshooting

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'openapi_client'`

**Solution**: Install the ny_benefits_oas package:
```bash
cd ny_benefits_oas
pip install -e .
```

### Authentication Errors

**Problem**: `Configuration Error: API credentials not provided`

**Solution**: 
1. Check that your `.env` file exists and contains credentials
2. Verify environment variables are loaded (use `python-dotenv`)
3. Or pass credentials directly to the tool

### API Connection Errors

**Problem**: Connection timeout or API unreachable

**Solution**:
1. Verify the API host URL is correct
2. Check your internet connection
3. Ensure the API service is running
4. Check if you need VPN or proxy access

### No Programs Found

**Problem**: Screening returns "No eligible programs found"

**Solution**: This is normal if eligibility criteria aren't met. Try:
- Adjusting income levels (lower income = more programs)
- Changing living situation (e.g., shelter, NYCHA)
- Modifying household composition

## Getting API Credentials

To obtain NYC Benefits API credentials:

1. Visit the NYC Benefits Screening API portal
2. Register for an account
3. Request API access
4. Receive your username and password

**Note**: The actual process may vary. Contact the API administrator for details.

## Next Steps

1. ✅ Complete installation
2. ✅ Configure credentials
3. ✅ Run test script
4. ✅ Try examples
5. 📖 Read the tool documentation: `src/ny_benefits_screener/tools/README.md`
6. 🚀 Build your own CrewAI agents!

## Additional Resources

- **Tool Documentation**: `src/ny_benefits_screener/tools/README.md`
- **CrewAI Documentation**: https://docs.crewai.com
- **OpenAPI Client Docs**: `ny_benefits_oas/docs/`
- **API Specification**: `nyc-benefits-screening-api.yml`

## Support

For issues or questions:
1. Check the tool README for detailed documentation
2. Review the examples for usage patterns
3. Consult the OpenAPI client documentation
4. Check CrewAI documentation for agent/task configuration

## Security Notes

⚠️ **Important Security Practices**:

1. **Never commit credentials** to version control
2. Add `.env` to `.gitignore`
3. Use environment variables for sensitive data
4. Rotate credentials regularly
5. Use different credentials for development/production
6. Limit API access to necessary IP addresses

## License

See the main project LICENSE file for details.