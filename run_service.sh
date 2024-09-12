#!/bin/bash

# activate virtual environment
source venv/bin/activate

#python3 gemma_service_main.py

cd gemma_service/
uvicorn gemma_service_main:app --reload