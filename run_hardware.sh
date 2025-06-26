#!/bin/sh

# # Get the absolute path to the script's directory
# SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# echo "Running script from: $SCRIPT_DIR"
#
# # Change to the script directory
# cd "$SCRIPT_DIR" || {
#   echo "Failed to cd into script directory: $SCRIPT_DIR"
#   exit 1
# }

# # Go to project directory
cd "$(dirname "$0")" || exit 1
# # cd /opt/apps/monitor || exit 1

# Print current directory after cd
echo "Current working directory: $(pwd)"

# Pull the latest changes
git pull

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate the virtual environment
# shellcheck disable=SC1091
. .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the target Python script
python3 manage.py hardware
