from pandagraph import Pandagraph
from pandagraph_demo_df import PandGraphDemoDf

Pandagraph(
    # PandGraphDemoDf.get_pandagraph_demo_df(from_date: int, to_date: int) -> pd.DataFrame
    PandGraphDemoDf(50000, 30).get_pandagraph_demo_df,

    # Sample parameters so we can get a tiny dataframe to examine
    from_date=20190101,
    to_date=20190601
).run()  # Run is a separate call because one may prefer to 'syndicate' the schema, i.e. make it part of a bigger one.
