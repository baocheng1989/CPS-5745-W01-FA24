import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"]

    def parse(self, response):
        cols = response.xpath('//*[@id="table3"]/thead/tr/th/span/text()').getall()
        for i in response.xpath('//*[@id="table3"]/tbody/tr'):
            yield {
                cols[0]: i.xpath('./td[1]/text()').get(), # Country
                cols[1]: int(i.xpath('./td[2]/text()').get().replace(',','')), # Cases
                cols[2]: int(i.xpath('./td[3]/text()').get().replace(',','')), # Deaths
                cols[3]: i.xpath('./td[4]/text()').get(), # Region
            }
