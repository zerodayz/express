#!/bin/bash

BASEDIR=$(basename $(pwd))

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color


if [ "$SHELL" = "/bin/zsh" ]; then
    SHELL_RC="${HOME}/.zshrc"
elif [ "$SHELL" = "/bin/bash" ]; then
    SHELL_RC="${HOME}/.bashrc"
else
    echo -e "${RED}Unsupported shell. Please use bash or zsh.${NC}"
    exit 1
fi

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

echo -e "${YELLOW}Creating files...${NC}"

if [ -f express/_custom.py ]; then
    echo -e "${YELLOW}Custom file already exists. Skipping...${NC}"
else
    echo -e "${YELLOW}Creating custom file...${NC}"
cat > express/_custom.py << EOF
class MyCustomActions:
    """
    This is your own class. You can add any functions you want to this class, and they will be available to all tests.
    """
    def __init__(self):
        pass

    def my_example_function(self, arg1):
        """
        This is my first example function. This function can be called from any test using the following syntax:

            actions.my_example_function("test")

        Args:
            arg1 (string): This is the first argument.

        Returns:
            None.
        """
        pass
EOF
fi

if grep -q "export PATH=\$PATH:$(pwd)" "${SHELL_RC}"; then
    echo -e "${YELLOW}Path already exists in ${SHELL_RC}. Skipping...${NC}"
else
    echo -e "${YELLOW}Adding path to ${SHELL_RC}...${NC}"
    echo "export PATH=\$PATH:$(pwd)" >> "${SHELL_RC}"
fi

echo -e "${GREEN}Done!${NC}"
echo ""
echo -e "Please restart your shell or run:"
echo -e "    source ${SHELL_RC}"
echo ""
echo -e "To get familiar with express execute:"
echo -e "    run.sh -h"
echo ""