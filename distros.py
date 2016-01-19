# -*- coding: utf-8 -*-
import scrapy

class DistrosItem(scrapy.Item):
    title = scrapy.Field()
    data = scrapy.Field()
    


class DistrosSpider(scrapy.Spider):
    name = "distros"
    allowed_domains = ["distrowatch.com"]
    start_urls = (
        'http://distrowatch.com/table.php',
    )

    def parse(self, response):
        for distro in response.xpath("//select/option/@value").extract():
            url = 'http://distrowatch.com/table.php?distribution={}'.format(distro)
            r= scrapy.Request(url,callback=self.parse_distro_page)
            r.meta['name']=distro
            yield r
    def parse_distro_page(self,response):
        item = DistrosItem()
        item['title']=response.meta['name']
        pyversions=response.xpath("//th/a[text()='Python']")[0].xpath("../../td/text()").extract()
        versions=response.xpath("//td[@class='TablesInvert']/text()").extract()
        # item['versiontable'] = zip(versions,pyversions)
        item['data']=[{'Distro_Version':dv,'Python_version':pv} for dv,pv in zip(versions,pyversions)]
        return item


