from .api import MercadoRadarAPI


class Site:
    @classmethod
    def list(cls, limit: int = 100, offset: int = 0) -> list:
        api = MercadoRadarAPI()
        return api.list_request(path=f'/v2/site/', limit=limit, offset=offset)
