#!/usr/bin/env bash
virtualenv colour_counter
source colour_counter/bin/activate
python3 ./setup.py
python3 ./colour_counter/app.py