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
chmod +x express-install && ./express-install
```
You should see:

```text
...
Done!

Please restart your shell or run:
    source <YOUR_HOME>/<SHELL_RC_FILE>

To get familiar with express execute:
    express-run -h

```

## Combination with Selenium IDE

Export the Python pytest from Selenium IDE and copy inside test folder.

```text
cp exported/test_login.py express/test/
```

## Run the tests

### Syntax

```bash
express-run -n|--number <tests_in_parallel> --headless --browser <browser1> --browser <browser2> <test_file.py>
```
### Examples
1. If you are not in a rush, you can run the tests sequentially on a single browser.
```bash
express-run --browser chrome test/test_example.py
```
2. If you want to run the tests in parallel on a single browser, you can use the -n option.

```bash
express-run -n 2 --browser chrome test/test_example.py
```
3. If you want to run the tests in parallel on multiple browsers, you can use the --browser option multiple times.
```bash
express-run -n 2 --browser chrome --browser firefox test/test_example.py
```
4. If you want to run the tests in parallel on multiple browsers in headless mode, you can use the --headless option.
```bash
express-run -n 2 --browser chrome --browser firefox --headless test/test_example.py
```

## Parallelism

For example if I execute `test/test_login.py` with 2 browsers and two accounts.

```bash
express-run --headless --browser chrome --browser firefox test/test_dropdown.py
```
It will factually run 2 tests per browser, so 4 tests in total.

The time is *17.01s* for these 4 tests. 

Now if instead I use `-n 4` to run 4 tests in parallel.

```bash
express-run --headless -n 4 --browser chrome --browser firefox test/test_login.py
```

The time is *8.42s* for the same 4 tests.

It is good improvement if you have too many tests to run.

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