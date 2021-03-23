# spider to make crawl and get necklace sets data

import scrapy
from ..items import HoinecklacesItem


url_domain = 'https://www.houseofindya.com{}'
url_extensions = ['/gold-kundan-red-drop-meena-earring-necklace-set-290/iprdt', '/gold-kundan-green-drop-pearl-earring-necklace-set-290/iprdt', '/floral-shaped-kundan-pendant-set-with-green-color-stone.-23/iprdt', '/gold-kundan-dual-pearl-earring-necklace-set-290/iprdt', '/white-diamond-aqua-drop-earring-necklace-set-290/iprdt', '/gold-leaf-kundan-double-pearl-earrings-necklace-set-290/iprdt', '/gold-kundan-blue-bead-pearl-earring-necklace-set-290/iprdt', '/white-diamond-floral-bunch-earring-necklace-set-290/iprdt', '/gold-textured-contemporary-choker-necklace-set-23/iprdt', '/silver-oxidized-green-stone-star-earring-necklace-set-290/iprdt', '/gold-kundan-green-drop-double-orb-earrinf-necklace-set-290/iprdt', '/dual-gold-kundan-green-bead-earring-necklace-set-290/iprdt', '/gold-kundan-blue-bead-earring-necklace-set-290/iprdt', '/blue-bead-kundan-earring-necklace-set-290/iprdt', '/gold-kundan-mangtika-earring-necklace-set-290/iprdt', '/gold-round-kundan-pearl-earring-necklace-set-290/iprdt',
                  '/white-blue-diamond-drop-string-earring-necklace-set-290/iprdt', '/gold-kundan-pearl-earring-necklace-set-290/iprdt', '/gold-kundan-tukdi-earring-necklace-set-290/iprdt', '/gold-kundan-multi-pearl-string-earring-necklace-set-290/iprdt', '/gold-plated-single-layer-squre-and-floral-shaped-kundan-necklace-set-23/iprdt', '/rose-gold-plated--crystal-necklace-set-23/iprdt', '/gold-kundan-green-bead-string-earring-necklace-set-290/iprdt', '/gold-kundan-pear-dainty-drop-earrings--necklace-set-290/iprdt', '/gold-kundan-multicolor-stone-earring-necklace-set-290/iprdt', '/floral-shaped-kundan-pendant-set-with-aqua-color-stone.-23/iprdt', '/gold-kundan-cascade-earring-necklace-set-290/iprdt', '/gold-red-kundan-bead-earring-necklace-set-290/iprdt', '/gold-orb-kundan-double-pearl-earrings-necklace-set-290/iprdt', '/dual-gold-kundan-pearl-earring-necklace-set-290/iprdt', '/white-blue-diamond-earring-pendant-necklace-set-290/iprdt', '/gold-green-kundan-bead-drop-earring-necklace-set-290/iprdt', '/gold-kundan-earring-pearl-string-pendant-necklace-set-290/iprdt']


class GetNeclaceSets(scrapy.Spider):
    name = 'necklace'
    allowed_domains = ['www.houseofindya.com']

    def start_requests(self):
        for item in url_extensions:
            url = url_domain.format(item)
            yield scrapy.Request(url)

    def parse(self, response, **kwargs):

        items = HoinecklacesItem()

        name = response.css('h1::text').get()
        price = response.css('.prodRight span:nth-child(3)::text').get()
        price = float(price)
        image = response.css(
            '.zoomli:nth-child(1) .lazySlider ::attr(data-original)').get()
        description = response.css('#tab-1 p::text').get()

        items['name'] = name
        items['price'] = price
        items['image'] = image
        items['description'] = description

        yield items
