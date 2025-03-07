import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadoLivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/cafeteira#D[A:cafeteira]"]

    def parse(self, response):
        pass
