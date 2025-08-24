# wit-code-guard

## Overview
The Code Analysis System is designed to automatically analyze Python files for code quality issues whenever a user runs the `wit push` command. This system integrates with a simplified version control system to ensure high-quality code is maintained across all commits. It uses Python's Abstract Syntax Tree (AST) for code analysis and generates visual graphs using Matplotlib to provide insights into the code quality.

## Installation and Execution Instructions
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/HadassaAvimorNew/code_quality_checker.git
   cd code_quality_checker
   ```

2. **Install Dependencies**: 
   Make sure you have Python installed, then install the required packages:
   ```bash
   pip install fastapi uvicorn matplotlib
   ```

3. **Run the Server**: 
   Start the FastAPI server:
   ```bash
   uvicorn main:app --host localhost --port 8000
   ```

4. **API Usage**: 
   You can now use the following endpoints to analyze Python files.

## Folder Structure
```
code_quality_checker/
│
├── main.py                   # FastAPI server and API endpoints
├── code_quality_checker.py    # Code analysis logic using AST
├── visualization.py           # Graph generation using Matplotlib
└── graphs/                    # Folder to store generated graphs
```

## API Endpoints

### 1. `/analyze`
- **Method**: POST
- **Description**: Accepts Python files and performs code analysis. Returns graphs representing the analysis.
- **Request**: Upload one or more Python files.
- **Response**: Returns a JSON object with the number of alerts for each file and generates graphs saved as PNG files.

### 2. `/alerts`
- **Method**: POST
- **Description**: Accepts Python files and returns warnings about code quality issues found in the files.
- **Request**: Upload one or more Python files.
- **Response**: Returns a JSON object containing the alerts for each file.

## Code Quality Checks
The system performs the following checks on each pushed Python file:
- **Function Length**: Warns if a function exceeds 20 lines.
- **File Length**: Warns if the entire file exceeds 200 lines.
- **Unused Variables**: Warns if a variable is defined but never used.
- **Missing Docstrings**: Warns if a function lacks a documentation string.

## Visual Graphs
The following graphs are generated based on the code analysis:
1. **Histogram**: Distribution of function lengths.
2. **Pie Chart**: Number of issues per issue type.
3. **Bar Chart**: Number of issues per file.
