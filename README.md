## Final Project

# Overview
This project implements an AI-powered software testing agent using 
the Model Context Protocol (MCP). The agent automatically:

- Runs Maven tests  
- Reads JaCoCo coverage  
- Generates new JUnit tests  
- Improves existing tests  
- Exposes hidden defects in the codebase  
- Fixes bugs when possible  
- Commits/pushes improvements to GitHub 
-Analyzes a real Java codebase

# Features implemented
MCP:
 - `run_tests()` : Runs `mvn test`, returns full output 
 - `get_coverage()` : Parses `target/site/jacoco/jacoco.xml` and returns line coverage 
 - `generate_test(class, method)` : Creates a basic JUnit test stub 
 - `git_status()` : Returns status of repo 
 - `git_add_all()` : Stages all files 
 - `git_commit(message)` : Commits changes 
 - `git_push(remote, branch)` : Pushes to GitHub 

 Stage 5 Tools:
 - `generate_boundary_tests(class, method, param_desc)` : Creates boundary-value + equivalence-class test scaffolds 
 - `simple_code_review(path)` : Scans for TODOs, debug prints, and common smells 

# Project Structure
codebase/
├── server.py 
├── main.py 
├── pom.xml
├── .github/
│ └── prompts/
│ └── tester.prompt.md 
├── src/
│ ├── main/java/... 
│ └── test/java/... 
├── target/
│ └── site/jacoco/... 
├── .venv2/ 
└── README.md 

# Installation and SetUp

1. git clone https://github.com/ActualEmmerz/Final_SE333.git
2. install uv + python venv 
    - uv venv
    - uv sync
3. Install MCP packages
    - uv add fastmcp mcp[cli] httpx
4. Run MCP server
    - uv run server.py
5. Connect server to VS code
6. Agent takes over
    - run_tests
    - get_coverage

# Troubleshooting
MCP server not showing in VS code:
    - Reload window: Ctrl+Shift+P -> Developer: Reload Window
No Coverage Report:
    - make sure pom.xml includes:
    <testFailureIgnore>true</testFailureIgnore>
    <argLine>--add-opens java.base/java.lang=ALL-UNNAMED</argLine>


# Repo Link
https://github.com/ActualEmmerz/Final_SE333.git