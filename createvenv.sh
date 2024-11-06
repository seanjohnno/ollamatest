#!/bin/bash

if [ ! -d './.venv' ];then
    python -m venv .venv
    echo """

PWD=\$(pwd)
export PYTHON_PATH=\$PWD
echo "PythonPath: \$PYTHON_PATH"
    """ >> ./.venv/bin/activate

    source ./.venv/bin/activate
    pip install -r requirements.txt
else
    source ./venv/bin/activate
fi
