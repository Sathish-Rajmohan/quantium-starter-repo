#!/bin/bash

venv/Scripts/python.exe -m pytest test_app.py

if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi