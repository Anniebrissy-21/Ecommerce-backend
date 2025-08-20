#!/usr/bin/env bash

set -o errexit  # Exit on any error

# Optionally activate your Python virtual environment
# source /path/to/your/venv/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
