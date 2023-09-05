from .api import MercadoRadarAPI
from datetime import date


class Product:
    @classmethod
    def list(cls,
             limit: int = 100,
             offset: int = 0,
             attributes_ids: list = None,
             category_ids: list = None,
             highest_price: float = None,
             lowest_price: float = None,
             product_names: list = None,
             seller_ids: list = None,
             site_ids: list = None,
             status: str = None) -> list:
        api = MercadoRadarAPI()
        params = cls.__set_params(attributes_ids=attributes_ids,
                                  category_ids=category_ids,
                                  highest_price=highest_price,
                                  lowest_price=lowest_price,
                                  product_names=product_names,
                                  seller_ids=seller_ids,
                                  site_ids=site_ids,
                                  status=status)
        return api.list_request(path='/v2/product/', limit=limit, offset=offset, params=params)

    @staticmethod
    def __set_params(attributes_ids,
                     category_ids,
                     highest_price,
                     lowest_price,
                     product_names,
                     seller_ids,
                     site_ids,
                     status: str) -> dict:
        params = dict()
        if category_ids:
            params['category_ids'] = ','.join(category_ids)
        if site_ids:
            params['site_ids'] = ','.join(site_ids)
        if attributes_ids:
            params['attributes_ids'] = ','.join(attributes_ids)
        if seller_ids:
            params['seller_ids'] = ','.join(seller_ids)
        if product_names:
            params['product_names'] = ','.join(product_names)
        params['status'] = status
        params['lowest_price'] = lowest_price
        params['highest_price'] = highest_price
        return params

    @classmethod
    def retrieve(cls, id: int) -> dict:
        api = MercadoRadarAPI()
        return api.retrieve_request(path='/v2/product/', id=id)

    @classmethod
    def history(cls, id: int,
                limit: int = 100,
                offset: int = 0,
                date__gte: date = None,
                date__lte: date = None) -> list:
        api = MercadoRadarAPI()
        params = dict()
        if date__gte:
            params['date__gte'] = date__gte.strftime('%Y-%m-%d')
        if date__lte:
            params['date__lte'] = date__lte.strftime('%Y-%m-%d')
        return api.action_request(path='/v2/product/', action='history', id=id, limit=limit, offset=offset, params=params)