import abc

class UrlHandlerFactory():
    def get_handler(url=''):
        if 'planetasport' in url:
            return PlanetaHandler

        if 'djaksport' in url:
            return DjakHandler

        if 'n-sport' in url:
            return NSportHandler

        if 'legend.rs' in url:
            return LegendHandler


class UrlHandler(metaclass=abc.ABCMeta):
    def __init__(self, data=None):
        self.data = data

    @abc.abstractmethod
    def get_price():
        pass

    def get_title(self):
        return self.data.title.string


class PlanetaHandler(UrlHandler):
    def get_price(self):
        price = self.data.find(attrs={'data-price-type': 'finalPrice'})
        return int(price.string[:-7].replace('.', ''))


class DjakHandler(UrlHandler):
    def get_price(self):
        price = self.data.find(class_='price-new')
        return int(price.string[:-8].replace('.', ''))

    def get_title(self):
        return self.data.title.string[3:-4]


class NSportHandler(UrlHandler):
    def get_price(self):
        price = self.data.find(class_='product-price')
        return int(price.string[:-4].replace('.', ''))


class LegendHandler(UrlHandler):
    def get_price(self):
        price = self.data.find(class_='product__price--regular-value')
        return int(price.string[:-3])