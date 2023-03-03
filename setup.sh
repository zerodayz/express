#!/bin/bash

BASEDIR=$(basename $(pwd))

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if [ "$BASEDIR" != "express" ]; then
    echo -e "${RED}Please run this script from the express directory.${NC}"
    exit 1
fi

if [ ! -d .venv ]; then
    echo -e "${YELLOW}Setting up virtual environment...${NC}"
    if ! python3 -m venv .venv
    then
        echo -e "${RED}Failed to create virtual environment.${NC}"
        exit 1
    fi
    echo -e "${GREEN}Virtual environment created.${NC}"
fi

echo -e "${YELLOW}Activating virtual environment...${NC}"
if ! source .venv/bin/activate
then
    echo -e "${RED}Failed to activate virtual environment.${NC}"
    exit 1
fi
echo -e "${GREEN}Virtual environment activated.${NC}"

echo -e "${YELLOW}Installing requirements...${NC}"
if ! python3 -m pip install --upgrade pip
then
    echo -e "${RED}Failed to upgrade pip.${NC}"
    exit 1
fi
if ! python3 -m pip install -r requirements.txt
then
    echo -e "${RED}Failed to install requirements.${NC}"
    exit 1
fi
echo -e "${GREEN}Requirements installed.${NC}"

echo -e "${GREEN}Done!${NC}"
echo ""
echo "Run 'source .venv/bin/activate' to activate the virtual environment."