# EXP Framework for Selenium

**Table of contents**

<img src="doc/express.png" width="202" height="202" border=0 align="right">

<!-- TOC depthfrom:1 insertanchor:false orderedlist:false -->

- [Introduction](#introduction)
- [Prepare the environment?](#prepare-the-environment)
- [Combination with Selenium IDE](#combination-with-selenium-ide)
- [Run the tests](#run-the-tests)
- [Collaborate](#collaborate)
- [Compatibility with Formy](#compatibility-with-formy)
- [Documentation](#documentation)
- [Contact us!!](#contact-us)

<!-- /TOC -->

## Introduction

This is a framework for Selenium tests written in Python. It is based on Selenium and pytest.

## Prepare the environment

```text
chmod +x setup.sh && ./setup.sh
```
You should see:

```text
...
Requirements installed.
Done!

Run 'source .venv/bin/activate' to activate the virtual environment.
```

## Combination with Selenium IDE

Export the Python pytest from Selenium IDE and copy inside test folder.

```text
cp exported/test_login.py express/test/
```

## Run the tests

Runs 4 tests in parallel with Chrome and Firefox browsers.

```python
python -m pytest -s -n 4 --browser=chrome --browser=firefox test/test_login.py
```


For example if you have 8 cores and 4 tests, you can run all tests for all browsers in parallel.

```python
python -m pytest -s -n 8 --browser=chrome --browser=firefox test/test_login.py
```

This can shorten the time of testings up to 3 times.

## Collaborate

## Compatibility with Formy
This is covering what tests are available and compatible with https://formy-project.herokuapp.com/.

- [ ] Autocomplete
- [ ] Buttons
- [x] Checkbox
- [x] Datepicker
- [x] Drag and Drop
- [ ] Dropdown
- [ ] Enabled and Disabled elements
- [ ] File Upload
- [ ] Key and Mouse press
- [ ] Modal
- [ ] Page Scroll
- [ ] Radio Button
- [ ] Switch Window
- [ ] Complete Web Form

## Documentation

You can first run the tests with Selenium IDE and then with use Express library to simplify the tests.

### Login with Selenium IDE
This is what the login example would look like in the test file:

```python
self.driver.get("http://127.0.0.1:8000/login")
self.driver.set_window_size(1364, 1055)
self.driver.find_element("name=username").click()
self.driver.find_element(By.NAME, "username").click()
self.driver.find_element(By.NAME, "username").send_keys("demo")
self.driver.find_element(By.NAME, "password").send_keys("demo")
self.driver.find_element(By.CSS_SELECTOR, ".w3-button").click()
```

### Login with Express and JSON file
```python
import pytest as pytest


@pytest.mark.parametrize(
    "credentials",
    [
        {
            "username": "demo",
            "password": "demo"
        },
        {
            "username": "admin",
            "password": "admin"
        }
    ],
)
def test_login(actions, credentials):
    actions.prepare_tests("test_login")
    actions.username = credentials["username"]
    actions.password = credentials["password"]

    actions.login(url="http://127.0.0.1:8000/login", submit="css=.w3-button")
```

### Taking screenshots
The screenshot will be saved into `out/test_login` directory.
```python
actions.take_screenshot("login.png")
```

### Taking screenshot of an element
Function `take_screenshot` can also take screenshot of an element as well the entire page.
```python
actions.take_screenshot("login.png", locator="css=#posts")
```

## Contact us