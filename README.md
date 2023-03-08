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

```bash
  _____  __  __  ____
 | ____| \ \/ / |  _ \ 
 |  _|    \  /  | |_) |
 | |___   /  \  |  __/
 |_____| /_/\_\ |_|   The Express Framework for Selenium

USAGE:
          run.sh -n|--number <tests_in_parallel> --headless --browser <browser1> --browser <browser2> <test_file.py>
EXAMPLES:

   If you are not in a rush, you can run the tests sequentially on a single browser.

          run.sh --browser chrome test/test_example.py

   If you want to run the tests in parallel on a single browser, you can use the -n option.

          run.sh -n 2 --browser chrome test/test_example.py

   If you want to run the tests in parallel on multiple browsers, you can use the --browser option multiple times.

          run.sh -n 2 --browser chrome --browser firefox test/test_example.py

   If you want to run the tests in parallel on multiple browsers in headless mode, you can use the --headless option.

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