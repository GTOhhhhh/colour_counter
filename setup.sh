#!/usr/bin/env bash
virtualenv colour_counter_env
source colour_counter_env/bin/activate
pip3 install
python3 setup.py install
python3 app.py