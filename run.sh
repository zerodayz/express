#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
WHITE='\033[0;37m'
PINK='\033[0;35m'
NC='\033[0m' # No Color

# Check directory using which run.sh
DIR=$(dirname $(which run.sh))

pushd "$DIR" >/dev/null || exit 1

# Check we are executed within express directory
BASEDIR=$(basename $(pwd))

if [ "$BASEDIR" != "express" ]; then
    echo -e "${RED}Please run this script from the express directory.${NC}"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d .venv ]; then
    echo -e "${RED}Virtual environment does not exist. Please run setup.sh first.${NC}"
    exit 1
fi

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
    echo -e "${WHITE}Listing:${NC}"
    echo -e ""
    echo -e "   List all available tests."
    echo -e ""
    echo -e "          run.sh -l"
    echo -e "${WHITE}Listing:${NC}"
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
    echo -e "   If you want to ignore a test, you can use the --ignore option."
    echo -e ""
    echo -e "          run.sh -n 9 --browser chrome --browser firefox --ignore '*recaptcha_v2*' test/"
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
        -l|--list)
            LIST=true
            shift
            ;;
        --browser)
            BROWSER+=("$2")
            shift
            shift
            ;;
        --ignore)
            IGNORE+=("$2")
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

echo -e "${PINK}  _____  __  __  ____${NC}"
echo -e "${PINK} | ____| \ \/ / |  _ \\ ${NC}"
echo -e "${PINK} |  _|    \  /  | |_) |${NC}"
echo -e "${PINK} | |___   /  \  |  __/${NC}"
echo -e "${PINK} |_____| /_/\_\ |_|${NC}   The Express Framework for Selenium"
echo -e ""

if [ $LIST ]; then
    echo -e "${YELLOW}Listing test files...${NC}"
    find test -name "test_*.py" -type f
    echo -e ""
    echo -e "To run a test file, use the following command:"
    echo -e ""
    echo -e "    run.sh <test_file.py>"
    echo -e ""
    exit 0
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
if ! source .venv/bin/activate
then
    echo -e "${RED}Failed to activate virtual environment.${NC}"
    exit 1
fi
echo -e "${GREEN}Virtual environment activated.${NC}"


# Set default variables
if [ -z "$HEADLESS" ]; then
    HEADLESS=false
fi
if [ -z "$BROWSER" ]; then
    BROWSER=("chrome")
fi

# Print variables
echo -e "${YELLOW}Running tests...${NC}"
echo -e "${GREEN}Number of cores allocated: $NUMBER${NC}"
echo -e "${GREEN}Headless: $HEADLESS${NC}"
echo -e "${GREEN}Browsers: ${BROWSER[@]}${NC}"
echo -e "${GREEN}Ignore: ${IGNORE[@]}${NC}"
echo -e "${GREEN}Test file: $TEST${NC}"

# Check if test file is directory
if [ -d "$TEST" ]; then
    echo -e "${GREEN}Test file is a directory.${NC}"
elif [ ! -f "$TEST" ]; then
    # Check if test file exists inside test directory
    if [ -f "test/$TEST" ]; then
        TEST="test/$TEST"
    else
        echo -e "${RED}Test file does not exist.${NC}"
        exit 1
    fi
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
for ignore in "${IGNORE[@]}"; do
    PYTEST_CMD="$PYTEST_CMD --ignore-glob=$ignore"
done
PYTEST_CMD="$PYTEST_CMD $TEST"

echo -e "${YELLOW}Pytest command: $PYTEST_CMD${NC}"

if ! $PYTEST_CMD
then
    echo -e "${RED}Failed to run tests.${NC}"
    exit 1
fi