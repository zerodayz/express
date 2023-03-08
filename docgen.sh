#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

if ! command -v sphinx-apidoc &> /dev/null
then
    echo -e "${RED}Please install sphinx-apidoc.${NC}"
    exit 1
fi

if ! command -v sphinx-build &> /dev/null
then
    echo -e "${RED}Please install sphinx-build.${NC}"
    exit 1
fi

if [ ! -d sphinx-docs ]; then
    echo -e "${RED}sphinx-docs directory was not found..${NC}"
    exit 1
fi

echo -e "${YELLOW}Generating documentation...${NC}"

pushd sphinx-docs
make markdown
popd
mv sphinx-docs/_build/markdown/express.md doc/DOCUMENTATION.md

echo -e "${GREEN}Documentation generated.${NC}"



