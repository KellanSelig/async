# Studies In Asynchronous Python

Studies to learn about writing asynchronous python code.

1. [random_number_generator](studies/random_number_generator.py)
   - Explore basic usage of python async/asyncio by finding random numbers that fall with a threshold. Also compares
     async vs sequential versions of running the same code to understand that effects, and uses colors to aid in 
     visualization


## Setup

```bash
poetry install
```

## Run examples:

```bash
export PYTHONPATH=$(pwd)
poetry run python <script>.py

# Can also do
poetry shell 
PYTHONPATH=$(pwd) run python <script>.py
```
