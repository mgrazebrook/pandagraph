from flask import Flask
from graphql_server.flask import GraphQLView
from pandagraph import Pandagraph
from tests.python.test_pandagraph import ages_df


app = Flask(__name__)

ages_schema = Pandagraph(ages_df, min_age=10, max_age=30).schema()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=ages_schema.graphql_schema,
    graphiql=True,
    graphql_version='1.2.0',
))

app.run()
