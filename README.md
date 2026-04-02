# connected-systems-tests
Automation framework for connecting multiple systems to validate the E2E journey 

## Running Tests
 ### Create a Fresh Virtual Environment
#### Mac / Linux
python3 -m venv test_env
source test_env/bin/activate

#### Windows
python -m venv test_env
test_env\Scripts\activate

### Install Dependencies from requirements.txt
pip install -r requirements.txt

### Install Playwright Browsers
playwright install

### Run Your Tests with headless
behave -f allure_behave.formatter:AllureFormatter -o allure-results

### Run Your Tests in headed mode
HEADLESS=False behave -f allure_behave.formatter:AllureFormatter -o allure-results

### Run the below command to open the test report
allure serve allure-results

## Test Evidence - Allure Test Report
The test results are shown in the Allure report screenshot at /evidence/Allure report.png. You can use this screenshot to see how the report looks like once tests ran successfully.