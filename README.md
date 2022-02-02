# pandagraph
From data frame to GraphQL API in 2 lines of code

Pandagraph is a Python library which introspects a Pandas database, uses that information to build 
a GraphQL API and exposes it through Flask.

We include a demo, a AngularJS application which uses the GraphQL to create several charts in a dashboard.

## Setting up Python

1. Download the current version of Python.
```shell
# Check you're running the right version:
python --version

# Create the virtual environment if you haven't already
python -m venv .venv

# Activate it: you should see '(.venv)' as part of the command line prompt
. .venv/bin/activate

pip install -r requirements.txt

# Run the tests (optional)
pytest --cov
```
