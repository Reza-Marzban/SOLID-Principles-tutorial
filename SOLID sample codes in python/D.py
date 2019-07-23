"""
Dependency Inversion Principle



Bad
Http is the high-level component, which is dependent on HttpService, the low-level component.
"""


class XMLHttpRequestService:
    pass


class XMLHttpService(XMLHttpRequestService):
    pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service

    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')


"""
better

Now, we are not dependent on the type of Http connection service passed to Http. it can easily connect to a network 
without bothering to know the type of network connection.
"""


class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError


class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')


class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options: dict):
        self.xhr.open()
        self.xhr.send()

"""
other types of connection:
"""

class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        pass

