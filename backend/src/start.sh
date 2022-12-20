#! /usr/bin/env sh

# If there's a prestart.sh script in the /app directory or other path specified, run it before starting
PRE_START_PATH=${PRE_START_PATH:-/src/prestart.sh}
echo "Checking for script in $PRE_START_PATH"
if [ -f "$PRE_START_PATH" ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

# Start Gunicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
