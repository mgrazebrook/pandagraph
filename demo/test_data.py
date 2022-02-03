import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from random import randrange


def make_monthly_data(revenue, employees):
    ret = {
        'id': [],
        'month': [],
        'revenue': [],
        'employees': [],
        'customers': [],
        'satisfaction': []
    }

    for row in range(24):
        ret['id'].append(row)
        ret['month'].append(20190000 + (row // 12 * 10000) + (row % 12 + 1) * 100 + 1)
        ret['revenue'].append(int(revenue * randrange(70, 130))/100)
        revenue *= randrange(80, 120) / 100
        ret['employees'].append(employees)
        employees += randrange(-6, 6)
        customers = int(revenue / 100 * randrange(50, 200) / 100)
        ret['customers'].append(customers)
        ret['satisfaction'].append(int((randrange(1, 5) + randrange(1, 5)) / 2))
    return ret


class StoreData:
    """
    The dataframe function can be a method, this lets you
    initialise the class with inputs which aren't from
    GraphQL.
    """
    def __init__(self, revenue, employees):
        data = make_monthly_data(revenue, employees)
        self.df = pd.DataFrame(data)

    def get_store_data(self, from_date, to_date):
        """
        Fake store data
        """
        return self.df[self.df.month.between(from_date, to_date)]


if __name__ == '__main__':
    store_data = StoreData(50000, 30)
