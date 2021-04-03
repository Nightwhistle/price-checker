class UrlHandlerFactory():
    def get_handler(url=''):
        if 'planetasport' in url:
            return PlanetaHandler

        if 'djaksport' in url:
            return DjakHandler
        
        if 'n-sport' in url:
            return NSportHandler


class UrlHandler():
    class Meta():
        abstract = True

    def get_price(data=None):
        pass
    
    def get_title(data=None):
        return data.title.string



class PlanetaHandler(UrlHandler):
    def get_price(data=None):
        price = data.find(attrs={'data-price-type': 'finalPrice'})
        return int(price.string[:-7].replace('.', ''))


class DjakHandler(UrlHandler):
    def get_price(data=None):
        price = data.find(class_='price-new')
        return int(price.string[:-8].replace('.', ''))
    
    def get_title(data=None):
        return data.title.string[3:-4]

class NSportHandler(UrlHandler):
    def get_price(data=None):
        price = data.find(class_='product-price')
        return int(price.string[:-4].replace('.', ''))

