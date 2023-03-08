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

Please see the [documentation](doc/DOCUMENTATION.md).

## Contact us