from .api import MercadoRadarAPI


class Attribute:
    @classmethod
    def list(cls, attribute_type: str, search: str = None) -> list:
        api = MercadoRadarAPI()
        return api.list_request(path=f'/v2/attribute/{attribute_type}/', params=dict(search=search))
