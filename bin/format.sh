#!/usr/bin/env bash

set -e

BOLD="\033[1m"
GREEN="\033[32m"
CYAN="\033[36m"
RESET="\033[0m"

echo -e "${CYAN}→ Running import checks...${RESET}"
uv tool run ruff check --select I --fix
echo -e "${GREEN}✓ Imports OK${RESET}"

echo -e "${CYAN}→ Formatting files...${RESET}"
uv tool run ruff format .
echo -e "${GREEN}✓ Formatting complete${RESET}"

echo -e "${BOLD}Done.${RESET}"