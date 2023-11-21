#!/usr/bin/env bash
DIRECTORY=virtualenvs/.py3
deactivate 2> /dev/null
if [ -d "${DIRECTORY}" ]; then
    source ${DIRECTORY}/bin/activate
else
    virtualenv -p `which python3.8` ${DIRECTORY}
    source ${DIRECTORY}/bin/activate
fi
