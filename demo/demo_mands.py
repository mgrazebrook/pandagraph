from pandagraph import Pandagraph
from test_data import StoreData

Pandagraph(
    # StoreData.get_store_data(from_date: int, to_date: int) -> pd.DataFrame
    StoreData(50000, 30).get_store_data,

    # Sample parameters so we can get a tiny dataframe to examine
    from_date=20190101,
    to_date=20190601
).run()  # Run is a separate call because one may prefer to 'syndicate' the schema, i.e. make it part of a bigger one.
