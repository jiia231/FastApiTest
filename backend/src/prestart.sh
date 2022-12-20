#! /usr/bin/env sh

export PYTHONPATH=src:${PYTHONPATH}

# Let the DB start
python3 ./app/pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python3 ./app/initial_data.py