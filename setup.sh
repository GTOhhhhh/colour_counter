#!/usr/bin/env bash
virtualenv colour_counter
source colour_counter/bin/activate
pip3 install .
python3 app.py