#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
WHITE='\033[0;37m'
PINK='\033[0;35m'
NC='\033[0m' # No Color

if [ $# -eq 0 ]; then
    echo -e "${PINK}  _____  __  __  ____${NC}"
    echo -e "${PINK} | ____| \ \/ / |  _ \\ ${NC}"
    echo -e "${PINK} |  _|    \  /  | |_) |${NC}"
    echo -e "${PINK} | |___   /  \  |  __/${NC}"
    echo -e "${PINK} |_____| /_/\_\ |_|${NC}   The Express Framework for Selenium"
    echo -e ""
    echo -e "${WHITE}USAGE:${NC}"
    echo -e "          run.sh -n|--number <tests_in_parallel> --headless --browser <browser1> --browser <browser2> <test_file.py>"
    echo -e "${WHITE}EXAMPLES:${NC}"
    echo -e ""
    echo -e "   If you are not in a rush, you can run the tests sequentially on a single browser."
    echo -e ""
    echo -e "          run.sh --browser chrome test/test_example.py"
    echo -e ""
    echo -e "   If you want to run the tests in parallel on a single browser, you can use the -n option."
    echo -e ""
    echo -e "          run.sh -n 2 --browser chrome test/test_example.py"
    echo -e ""
    echo -e "   If you want to run the tests in parallel on multiple browsers, you can use the --browser option multiple times."
    echo -e ""
    echo -e "          run.sh -n 2 --browser chrome --browser firefox test/test_example.py"
    echo -e ""
    echo -e "   If you want to run the tests in parallel on multiple browsers in headless mode, you can use the --headless option."
    echo -e ""
    echo -e "          run.sh -n 2 --browser chrome --browser firefox --headless test/test_example.py"
    echo -e ""
    exit 1
fi

while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -n|--number)
            NUMBER="$2"
            shift
            shift
            ;;
        --browser)
            BROWSER+=("$2")
            shift
            shift
            ;;
        --headless)
            HEADLESS=true
            shift
            ;;
        *)
            TEST="$1"
            shift
            ;;
    esac
done

# Set default variables
if [ -z "$HEADLESS" ]; then
    HEADLESS=false
fi
if [ -z "$BROWSER" ]; then
    BROWSER=("chrome")
fi

# Print variables
echo -e "${YELLOW}Running tests...${NC}"
echo -e "${GREEN}Number of tests in parallel: $NUMBER${NC}"
echo -e "${GREEN}Headless: $HEADLESS${NC}"
echo -e "${GREEN}Browsers: ${BROWSER[@]}${NC}"
echo -e "${GREEN}Test file: $TEST${NC}"

# Check if test file exists
if [ ! -f "$TEST" ]; then
    echo -e "${RED}Test file does not exist.${NC}"
    exit 1
fi

# Construct pytest command
PYTEST_CMD="python3 -m pytest"
if [ -n "$NUMBER" ]; then
    PYTEST_CMD="$PYTEST_CMD -n $NUMBER"
fi
if $HEADLESS; then
    PYTEST_CMD="$PYTEST_CMD --headless"
fi
for browser in "${BROWSER[@]}"; do
    PYTEST_CMD="$PYTEST_CMD --browser=$browser"
done
PYTEST_CMD="$PYTEST_CMD $TEST"

echo -e "${YELLOW}Pytest command: $PYTEST_CMD${NC}"

if ! $PYTEST_CMD
then
    echo -e "${RED}Failed to run tests.${NC}"
    exit 1
fi