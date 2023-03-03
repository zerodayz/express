# Express Framework for Selenium

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
cp exported/test_rusty.py express/test/
```

Add the folowing line above the test class:
```python
from src import express
```

## How to use

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
def test_express(actions, credentials):
    actions.prepare_tests("test_express")
    actions.username = credentials["username"]
    actions.password = credentials["password"]

    actions.login(url="http://127.0.0.1:8000/login", submit="css=.w3-button")

    actions.take_screenshot("login.png")
    actions.go("http://127.0.0.1:8000/logout")
```

### Taking screenshots
The screenshot will be saved into `out/test_express` directory.
```python
actions.take_screenshot("login.png")
```

### Taking screenshot of an element
Function `take_screenshot` can also take screenshot of an element as well the entire page.
```python
actions.take_screenshot("login.png", locator="css=#posts")
```