from .api import MercadoRadarAPI


class AttributeType:
    @classmethod
    def list(cls, limit: int = 100, offset: int = 0) -> list:
        api = MercadoRadarAPI()
        return api.list_request(path='/v2/attribute-type/', limit=limit, offset=offset)
