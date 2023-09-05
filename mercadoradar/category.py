from .api import MercadoRadarAPI


class Category:
    @classmethod
    def list(cls, limit: int = 100, offset: int = 0, search: str = None) -> list:
        api = MercadoRadarAPI()
        return api.list_request(path='/v2/category/', limit=limit, offset=offset, params=dict(search=search))

    @classmethod
    def retrieve(cls, id: int) -> dict:
        api = MercadoRadarAPI()
        return api.retrieve_request(path='/v2/category/', id=id)
