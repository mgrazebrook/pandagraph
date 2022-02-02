import graphene


def py_to_graphql_type(sample_value):
    return {
        str: graphene.String(),
        int: graphene.Int(),
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
        return self.dataframe_function.__doc__.strip()

    def schema(self):
        """
        Build the GraphQL schema: one type and one query.

        :return: graphene.Schema
        """
        object_type = type(self.type, (graphene.ObjectType,), self.columns)

        # TODO: Can I introspect default params? For now, parameters are optional.
        #  but they should really only be optional if the dataframe function has default params.
        #  e.g. graphene.Int(required=True)
        query_attributes = {self.type: graphene.Field(object_type, **self.query_args)}
        query = type(self.type + 'Query', (graphene.ObjectType,), query_attributes)

        return graphene.Schema(query=query)
