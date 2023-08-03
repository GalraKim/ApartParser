from urllib import response
import scrapy
import time

class AppartSpider(scrapy.Spider):
    name = "Appart Spider"
    start_urls=["https://tomsk.besposrednika.ru/?site={}"]

    def parse(self, response):
            k=0

            start_urls="https://tomsk.besposrednika.ru/?site={}"
            while k<8:
                k=k+1
                links = response.css('div.adListing link::attr(href)').getall()
                for link in links:
                    time.sleep(3)
                    yield response.follow(link, self.parse_appart)
                link = start_urls.format(k)
                yield response.follow(link, self.parse)

    def parse_appart(self, response):
        yield {
            "name": response.css("div.sEnLiTitle h1::text").get(),
            "price": response.css('span[itemprop="price"]::attr(content)').get(),
            "adress": response.css('div.sEnLiCity span::text').get(),
            "description": response.css('div.sEnLiDescription::text').get(),
            "aboutHouse":response.css("span.value::text").getall(),
            # "floor": response.css("span.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_6u--A1GMI.a10a3f92e9--fontWeight_bold--ePDnv.a10a3f92e9--fontSize_16px--RB9YW.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG::text").get(),
            # "area": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_22px--bnKK9.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_16px--RB9YW.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            # "comunpayment": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_20px--tUURJ.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_14px--TCfeJ.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            # "renovation": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_22px--bnKK9.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            # "deposit": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_20px--tUURJ.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_14px--TCfeJ.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            # "comission": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_20px--tUURJ.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_14px--TCfeJ.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            # "typeOfHouse": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_22px--bnKK9.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_16px--RB9YW.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            # "covering": response.css("p.a10a3f92e9--color_black_100--kPHhJ.a10a3f92e9--lineHeight_22px--bnKK9.a10a3f92e9--fontWeight_normal--P9Ylg.a10a3f92e9--fontSize_16px--RB9YW.a10a3f92e9--display_block--pDAEx.a10a3f92e9--text--g9xAG.a10a3f92e9--text_letterSpacing__normal--xbqP6::text").get(),
            
            }