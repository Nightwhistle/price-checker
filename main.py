import pandas as pd
from tabulate import tabulate

from products import PRODUCTS
from Client.client import Client


def main():
    print_header()

    calculated_data = []
    for artikal in PRODUCTS:
        client = Client(artikal['url'])
        data = client.get_data()

        calculated_data.append(calculate_data(
            data, artikal)) if calculate_data(data, artikal) else None

    df = pd.DataFrame(calculated_data)
    table = tabulate(df, showindex=False,
                     headers=df.columns, tablefmt='presto')

    print(table) if len(calculated_data) else print('NOTHING FOUND!')

    print_footer()


def calculate_data(data, artikal):
    if artikal['wanted_price'] >= data['price']:
        return {
            'wanted': artikal['wanted_price'],
            'price': data['price'],
            'title': data['title'],
            'link': artikal['url']
        }


def print_header():
    print('*****************************************************************************')
    print('*                             CHECKING PRICES ')
    print('*')
    print('*')


def print_footer():
    print('*')
    print('*                            CHECKING COMPLETED')
    print('*****************************************************************************')


if __name__ == '__main__':
    main()
