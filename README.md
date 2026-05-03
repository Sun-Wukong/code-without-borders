# Code Without Borders: Smooth Sailing Solutions
 
Building deployment ready apps w/o writing code

**Problem Statement**

* We address the challenge of consistently delivering quality code with Agentic solutions
    * Foundational language models, no matter how advanced, have a chance of hallucinating output
    * This results in reduced quality of delivered software in the best case, and hard to track bugs and vulnerabilities at the worst
    * Considering the consumption models for AI services, this also has growing financial implications
* This affects AI users across all backgrounds and skill levels
    * Technical users and non-technical folks are both at risk of receiving incorrect outputs from AI and may not realize it until it becomes costly to correct
* Considering the business needs for increased agility with smaller staff counts, this urgency is compounded by the non-deterministic nature of Generative and Agentic AI technology
    * Less staff altogether means less specialists, bandwidth, and resilience to the unknown(under those circumstances), in exchange for increase workloads per staff member
    * Without a series of corrective rules, guidelines, and quality control assets, this becomes something similar to scope creep


## Solution Overview

 By structuring how IBM Bob operates through skill specification, agents and OpenAPI description (the NYC Benefits Screening YML File), the solution ensures AI becomes a dependable engineering teammate rather than an unpredictable tool, helping teams do more with less. While also making critical services more accessible to real people who need them most. 

### Key features

1. Structured AI Agent Skills 

Giving Bob step-by-step recipe, Skills specifications as a guide. 

1. Hallucination Reduction 

Structured rules and guideline, creating consistency.

2. Guided Solution Engineering 

Bob is methodically walked through a guide instead of being told “build me something”

3. Works for All Skill Levels 

Technical and non- technical can rely on the outputs, due to quality no matter the level of the user. 

4. Cost Control 

Reducing hallucinations and bad outputs, reduces financial cost of fixing mistakes. 

5. Real- World Application

Applied to NYC Benefits Screening, making Government benefit information accessible via chats  without needed a computer. 

6. Agentic coding via Spec Driven Development

Working primarily through skill specs, agent personas and OpenAPI/ YML files rather than writing large code, makes it accessible for smaller teams.

7. Optional architecture diagram

Similar to _Design Language_, diagrams serve as a common communication medium of expectations for people and AI alike

### How IBM Bob Was Used

*  We used about 3 task sessions to produce our solution
    * Total reported Bob token cost came in at under 10 tokens, less than 25% of the individual contributor budget and just above 5% of the team budget
    * Compared to teams that exhausted their budgets before submission, this makes a compelling statement for efficiency
* Using a combination of agent definitions, agent skills, API documentation(OpenAPI), and generated API client code...
    * We were able to create a properly documented, containerized instance of a CrewAI application
    * We were also able to extend the base CrewAI application with a custom tool connected to a 3rd party web service
* Bob reports and screenshot of majority token consumption may be found at bob-report/ in the project root directory


**watsonx.ai / watsonx Orchestrate Integration**

* WatsonX is the LLM provider for our CrewAI Agentic application
* The CrewAI application is an example of what can be generated with our solution
    * Using the app require getting credentials from the NYC Benefits Screening API, which takes a few hours to a few days for approval
    * This also applies to receiving test credentials


## Getting Started / Installation

### Dependencies
- CrewAI example app
    - Recent `docker` installation
    - NYC Benefits Screening API Credentials
    - Infrastructure Architect Agent
        - Bob IDE
        - Bob Shell
        - Other LLM harnesses capable or reading Agentskills specifications
### Quickstart(Creating a multi-container application)
  - If you don't have an app on hand, start a planning session by asking to design a multi-container solution
  - Make a copy of the `mystack.csv` spreadsheet found at `.bob/skills/design-container-solution/references/` and fill it out with details for each container you want to use
  - Submit the new CSV file to the agent
  - Confirm the generated Mermaid chart and docker-compose files are to your liking


### Usage / Demo

  - [Spec Driven Workflow with CrewAI screenshots](https://1drv.ms/f/c/510f70fcb0215849/IgDQLpLsJYh5SqhR1G5X0PjVActaulUUKdx0KPXw_FxsWrE?e=ZRiPVg)
  - [Video walkthrough of generating container solution via prompting](https://1drv.ms/v/c/510f70fcb0215849/IQDHHT9xKGfnQL8F8agdkbhVAfRdboYmn9HwkCYHR_MNTwM?e=pOhO5X)


### Project Structure
 - `.bob`: Bob skills at `skills` and notes at `notes`
 - `bob-reports`: location of reports, Bobalytics, and screenshots
 - `ny-benefits-screener`: location of CrewAI app
 - `ny-benefits-screener/dockerfile`: dockerfile for NY-Benefits-Screener
- `ny-benefits-screener/README.md`: README and start up instructions for NY-Benefits-Screener
- `AGENTS.md`: Sub agent details for `infrastructure-architect` subagent
-`ny-benefits-oas`: API Client for `ny-benefits-screener`
- `ny-benefits-oas/README.md`: README and start up instructions for NY-Benefits-OAS

### Team Members
- Jason Scoon|Team Lead: Coding, documentation, and project planning 
- Tarcia Pillows| Team Member: reasearch, documentation, project planning, support across all areas of project 
- Salman Abiola Suleiman| Team Member: reasearch, project planning, support across all areas of project 
- Vincent Jared| Team Member: reasearch, project planning, support across all areas of project 

### License
 • MIT

### Acknowledgments

- CrewAI
- OpenAPI
- OpenAPI-generator
- agentskills.io
- mermaid.ai 



* Contact / Support (optional)
 • Team Lead may be reached at jasonc.scoon@gmail.com



