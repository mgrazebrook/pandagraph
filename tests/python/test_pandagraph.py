import pytest
import pandas as pd
from pandagraph import Pandagraph


def ages_df(min_age=18, max_age=70):
    df = pd.DataFrame({'name': ['Alice', 'Bill', 'Charlie'], 'age': [27, 42, 39]})
    return df[df.age.between(min_age, max_age)]


def test_introspection_reads_function_name_params_columns_types():
    """
    pandagraph introspects a function creating a dataframe.

    The GraphQL type is the function name.
    The query parameters are the function parameters.
    The type's attribute are the column names.
    The attribute types map from Pandas types to GraphQL types.
    """
    pg = Pandagraph(ages_df, min_age=20, max_age=30)
    assert pg.type == 'ages_df'
    assert pg.columns == {'name': 'String', 'age': 'Int'}
    assert pg.query_args == {'min_age': 'Int', 'max_age': 'Int'}
