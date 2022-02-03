import pytest
import pandas as pd
import graphene
from pandagraph import Pandagraph
from flask import Flask
from graphql_server.flask import GraphQLView


def ages_df(min_age=18, max_age=70):
    """
    Names and ages for testing.
    """
    df = pd.DataFrame({'name': ['Alice', 'Bill', 'Charlie', 'Deidre'], 'age': [27, 42, 39, None]})
    return df[df.age.between(min_age, max_age)]


def test_introspection():
    """
    pandagraph introspects a function creating a dataframe.

    The GraphQL type is the function name.
    The query parameters are the function parameters.
    The type's attribute are the column names.
    The attribute types map from Pandas types to GraphQL types.
    """
    # Parameters which return just one row
    pg = Pandagraph(ages_df, min_age=20, max_age=30)
    assert pg.type == 'ages_df'
    assert pg.columns == {'name': graphene.String(), 'age': graphene.Float()}
    assert pg.query_args == {'min_age': graphene.Int(), 'max_age': graphene.Int()}
    assert pg.comment == ages_df.__doc__.strip()


def test_schema_execute_simple_query():
    pg = Pandagraph(ages_df, min_age=20, max_age=30)
    schema = pg.schema()

    query = """"query fetch {
        ages_dfQuery(min_age: 0, max_age: 40)
    }"""
    query = '{ ages_dfQuery(min_age: 0, max_age: 40) }'
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {"ages_dfQuery": [{"name": "Alice"}, {"name": "Charlie"}]}
