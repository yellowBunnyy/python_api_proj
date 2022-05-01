#!/bin/bash
echo "Start Runed script file!!"
python create_db.py
python -m flask run --host=0.0.0.0 --port=5000
