import scrapy

class MPPOntarioSpider(scrapy.Spider):
    name = 'mppontario'
    start_urls = ['https://www.ola.org/en/members/current/contact-information']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)
