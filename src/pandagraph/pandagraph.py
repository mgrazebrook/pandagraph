import graphene
from datetime import datetime


def py_to_graphql_type(sample_value):
    return {
        str: graphene.String(),
        int: graphene.Int(),
        datetime: graphene.DateTime(),
    }[sample_value.__class__]


def pandas_to_graphql_type(dtype_name, example=None):
    """
    Convert pd.dtypes types to GraphQL types.

    :param dtype_name: Pandas data type name
    :param example: Not yet used, may be used to work out what an Object really is.
    :return:
    """
    return {
        'object': graphene.String(),
        'int64': graphene.Int(),
        'float64': graphene.Float(),
        'datetime64[ns]': graphene.DateTime(),  # TODO: "Invalid comparison between dtype=datetime64[ns] and datetime"
    }[dtype_name]


class Pandagraph:
    def __init__(self, dataframe_function, **kwargs):
        """
        :param dataframe_function: A function returning a Pandas dataframe
        :param kwargs: A sample set of args returning a tiny example - one row is enough, just something to inspect

        The sample args need to be sufficient to return a sample dataframe for us to inspect. We need column names and
        their data types. If it has at least one row, we may use the data in it to work out if an object datatype is
        really a string.
        """
        self.dataframe_function = dataframe_function
        self.kwargs = kwargs
        self.sample = dataframe_function(**kwargs)

    @property
    def type(self):
        return self.dataframe_function.__name__

    @property
    def columns(self):
        return {
            name: pandas_to_graphql_type(pandas_type.name, None if len(self.sample) == 0 else self.sample[name][0])
            for name, pandas_type
            in self.sample.dtypes.items()
        }

    @property
    def query_args(self):
        return {
            name: py_to_graphql_type(sample_value)
            for name, sample_value
            in self.kwargs.items()
        }

    @property
    def comment(self):
        if self.dataframe_function.__doc__ is None:
            return ''
        return self.dataframe_function.__doc__.strip()

    # def _query_resolver(self, parent, info, **args):
    #     # May not work: 'Graphene executes this as a staticmethod implicitly'
    #     # https://docs.graphene-python.org/en/latest/types/objecttypes/
    #     df = self.dataframe_function(**args)
    #     return df.itertuples()

    def schema(self):
        """
        Build the GraphQL schema: one type and one query.

        :return: graphene.Schema
        """
        object_type = type(self.type, (graphene.ObjectType,), self.columns)

        # TODO: Can I introspect default params? For now, parameters are optional.
        #  but they should really only be optional if the dataframe function has default params.
        #  e.g. graphene.Int(required=True)

        # TODO: , **self.query_args

        query_attributes = {
            "rows": graphene.List(
                graphene.NonNull(object_type),
                description=self.comment,
                args=self.query_args,
            ),
            # A resolver is automatically a static method: no access to self
            "resolve_rows": lambda parent, info, **kwargs: self.dataframe_function(**kwargs).itertuples()
        }
        query = type('Query', (graphene.ObjectType,), query_attributes)

        return graphene.Schema(query=query)
