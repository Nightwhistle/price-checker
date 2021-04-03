from Client.handlers import UrlHandlerFactory
from bs4 import BeautifulSoup
import urllib.request


class Client:
    def __init__(self, url=''):
        self.url = url

    def get_data(self):
        fp = urllib.request.urlopen(self.url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        fp.close()

        soup = BeautifulSoup(mystr, 'html.parser')

        response_handler = UrlHandlerFactory.get_handler(url=self.url)
        return {
            'price': response_handler.get_price(data=soup),
            'title': response_handler.get_title(data=soup),
        }