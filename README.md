# pandagraph
From data frame to GraphQL API in 1 line of code (+ imports)

Pandagraph could be used for rapidly prototying data science in a web front end or building dasboards. It turns
a dataframe into a GraphQL API. It's designed so you can "federate" it as part of a larger GraphQL schema for
production use.

Pandagraph introspects a method returning a Pandas data frame. The function name becomes the query name; the function 
parameters become query parameters; the column definitions become the GraphQL type.

We include a [demo](https://github.com/mgrazebrook/pandagraph-web-app), a AngularJS application which uses the GraphQL to create several charts in a dashboard.

This project is mostly very simple applications of a technology stack so it could also be used for learning:

Pandas - Python introspection - Graphene - Flask - GraphQL - Python packaging - (and in the front end) - Angular -  PrimeNG

## Example of use
```python
from pandagraph import Pandagraph
from my_datascience import CleverStuff, data_sources

Pandagraph(
    # Assuming your method has a signature like this:
    # CleverStuff.get_dataframe(query_param: str) -> pd.DataFrame
    # 
    # It can take a function. Here, I've shown it using a method so
    # you can construct your class with any parameters which you need to create your dataframe
    # The method name is the query name. Its docstring is help text.
    CleverStuff(data_sources).get_dataframe, 
    
    # query_param is a stand-in for as many query parameters as you want: it's kwargs
    # Pandagraph needs to introspect a sample dataframe when it is constructed.
    # So you need to give it parameters which, on your function, rerurn a sample dataframe (one row is enough)
    query_param='FilterValue',
).run()  # Run is a separate call because one may prefer to 'syndicate' the schema, i.e. make it part of a bigger one.
```

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
Why do my query and type have the same name?
If a DF has a name, how can I link it to an object in a federated schema?
Improve the README: a bit more sales pitchy at the start, notes on production use