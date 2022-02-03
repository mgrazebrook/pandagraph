# pandagraph
From data frame to GraphQL API in 2 lines of code

Pandagraph is a Python library which introspects a Pandas database, uses that information to build 
a GraphQL API and exposes it through Flask.

We include a demo, a AngularJS application which uses the GraphQL to create several charts in a dashboard.

## Setting up Python

Download the current version of Python if you don't have a recent version (3.7+?)

```shell
# Check you're running the right version:
python --version

# Create the virtual environment if you haven't already
python -m venv .venv

# Activate it: you should see '(.venv)' as part of the command line prompt
. .venv/bin/activate

pip install -r requirements.txt

# Run the tests (optional). Using pytest directly may result in it running in another environment.
python -m pytest --cov

# Run the demo server:
python demop.py
```
Your dataframe should now be exposed here: http://127.0.0.1:5000/graphql

## References
### The tech stack
This project consists of a chained set of simple steps constituting a tech stack. So it could be used as a template
to be adapted or for learning.
1. Pandas: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
2. Python introspection: https://docs.python.org/3/library/inspect.html
3. GraphQL: https://graphql.org/learn/
4. Graphene, for building a graphQL schema in Python: https://docs.graphene-python.org/en/latest/
5. Flask-graphQL integration: https://github.com/graphql-python/graphql-server/blob/master/docs/flask.md
7. Flask for the web API: https://palletsprojects.com/p/flask/
8. Packaging Python projects, to make it a lib on PyPi: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## See also:
1. Relay - a graphQL client recommended from graphene: https://relay.dev
2. Ariadne - a schema first alternative for Python/GraphQL: https://ariadnegraphql.org

## TODO:
Return a list of row objects not a single object.
