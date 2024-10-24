Read me file

# Project Title

Test automation script for linkedin login page

## Description

This project is designed to test linkedin login page using Python Selenium. 
It supports multiple browsers including Chrome, Firefox, Edge, and Safari. The browser type is configured via a CSV file.
Testdata is stored in a testdata.csv

## Code Structure

The project is organized as follows:

- `test_cases/`: Contains the test scripts.
  - `test_driven_data.py`: Main test script for LinkedIn login page.
- `Utils/`: Contains utility modules.
  - `config_helper.py`: Helper module for reading browsers configuration from CSV.
  - `csv_helper.py`: Helper module for reading test data from CSV.
- `pages/`: Contains page object models.
  - `login_page.py`: Page object model for the LinkedIn login page.
  - `home_page.py`: Page object model for the LinkedIn home page.
- `helpers/`: Contains helper modules.
  - `browser_actions.py`: Helper module for browser actions
  - `driver_actions.py`: Helper module for WebDriver initialization.
- `requirements.txt`: Lists the dependencies required for the project.
- `Dockerfile`: Defines the Docker image for the project.
- `docker-compose.yml`: Defines the Docker services for the project.
- `README.md`: Provides an overview and instructions for the project.
- `testdata.csv`: Contains test data for the login tests.



## Installation

1. **Clone the repository**:
    git clone https://github.com/Andyalbert23811/XischeTask

2. **Create a virtual environment**:
    python3 -m venv .venv
    source .venv/bin/activate

3. **Install the dependencies**:
    pip install -r requirements.txt
4. **Run the test**:
    python test_cases/test_driven_data.py
5. **Using Docker**:  
Build the Docker image:  
docker build -t linkedin-login-test .
Run the Docker container:  
docker run --rm -v $(pwd):/app linkedin-login-test
