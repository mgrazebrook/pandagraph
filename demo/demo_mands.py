from flask import Flask
from graphql_server.flask import GraphQLView
from pandagraph import Pandagraph
from datetime import datetime

from test_data import StoreData

app = Flask(__name__)

schema = Pandagraph(StoreData(50000, 30).get_store_data, from_date=20190101, to_date=20190601).schema()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema.graphql_schema,
    graphiql=True,
    graphql_version='1.2.0',
))

app.run()
