import csv

from .api import MercadoRadarAPI
from datetime import date


class Export:
    @classmethod
    def product_history(cls, date: date):
        api = MercadoRadarAPI()
        date_str = date.strftime('%Y-%m-%d')
        content = api.list_request(path=f'/v2/export/product-history/{date_str}/')
        filename = f'MERCADORADAR_PRODUCT-HISTORY_{date_str}'
        cls.__save_csv(filename=filename, content=content)

    @staticmethod
    def __save_csv(filename: str, content: bytes):
        content_str = content.decode('utf-8')
        with open(f'{filename}.csv', 'w') as file:
            writer = csv.writer(file)
            rows = content_str.strip().split('\n')
            for row in rows:
                columns = row.split(',')
                writer.writerow(columns)
