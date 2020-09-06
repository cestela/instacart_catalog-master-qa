# Instacart Crawler - QA

Instacart Crawler QA is a testing automation project for the Instacart Crawler app. 

This project is ready to be pushed to Git repository and to be integrated in a CI/CD pipeline.

## Project Structure

```bash
.
├── Configurations
├── Logs
├── Reports
├── Screenshots
├── pageObjects
├── testCases
└── utilities
```
* **Configurations**: This directory includes the common data configuration shared among the test cases.

* **Logs**: This directory includes a log file with the results of each test chronologically ordered.

* **Reports**: This directory includes the generated Pytest html reports created at the end of the test suite execution.

* **pageObjects**: This package includes the POM classes representing the DOM structure and interaction of the application.

* **testCases**: This package includes all the test cases and their configurations.

* **utilities**: This package includes tools to read Configurations properties and a custom logger.


## Preconditions

1. Install the dependencies found in `requirements.txt`

2. Make sure you have all the Selenium WebDrivers needed for the tool to work (Chrome and Firefox). You can find the WebDrivers [here](https://pypi.org/project/selenium/).

3. Make sure to set the env PATH properly in order for Selenium to find the WebDriver. More info on this [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

4. Since the tests are running on a local execution of the application, it is important to make sure that the application is running locally and can be located in the following url: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

5. Make sure to update the `sessionCookie` on `Configurations/config.ini` before running the tests in order to ensure that the sessionCookie is not expired.



## Test Execution

### 
 To run the tests you can either execute the `windowsRun.bat` / `unixRun.sh` (depending on the operating system) or execute the Pytest command on the terminal:

```bash
pytest -v -s -m "regression" -n=3 --html=Reports/report_chrome.html --browser chrome
```
### Params explained
```bash
-m "regression"
```
This parameter allows the test cases to be executed depending of the associated group. Possible values:
* **"sanity"** : Basic set of test cases to ensure application is working.

* **"regression"** : Set of test cases to ensure that previously developed and tested software still performs after a change.

```bash
-n=3
```
This parameter allows to establish multithreads for the parallelized execution of the tests. Increasing this amount may result in low performance.

```bash
--html=Reports/report.html
```
This parameter allows the generation of a html report file in the Reports directory when the test suite execution is finished.

```bash
--browser chrome
```
This parameter allows the user to choose on what webdriver should the test cases be executed.Possible values:
* **chrome** : Executes chrome webdriver.

* **firefox** : Executes fiefox webdriver.