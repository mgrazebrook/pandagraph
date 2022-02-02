from flask import Flask
from flask_graphql import GraphQLView
from pandagraph import Pandagraph
from tests.python.test_pandagraph import ages_df


app = Flask(__name__)

ages_schema = Pandagraph(ages_df, min_age=10, max_age=30).schema()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=ages_schema,
    graphiql=True
))

app.run()
