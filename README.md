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

### Syntax

```bash
run.sh -n|--number <tests_in_parallel> --headless --browser <browser1> --browser <browser2> <test_file.py>
```
### Examples
1. If you are not in a rush, you can run the tests sequentially on a single browser.
```bash
run.sh --browser chrome test/test_example.py
```
2. If you want to run the tests in parallel on a single browser, you can use the -n option.

```bash
run.sh -n 2 --browser chrome test/test_example.py
```
3. If you want to run the tests in parallel on multiple browsers, you can use the --browser option multiple times.
```bash
run.sh -n 2 --browser chrome --browser firefox test/test_example.py
```
4. If you want to run the tests in parallel on multiple browsers in headless mode, you can use the --headless option.
```bash
run.sh -n 2 --browser chrome --browser firefox --headless test/test_example.py
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
- [x] Dropdown
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