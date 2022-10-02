from spider_for_NASA import Spider

url = "https://ntrs.nasa.gov/search?sort=%7B%22field%22:%22published%22,%22order%22:%22desc%22%7D"
url_json = "https://ntrs.nasa.gov/api/citations/search?keyword=International%20Space%20Station"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

spider = Spider(url=url_json, headers=headers)
# with open('./html.txt','w') as f:
#     f.write(spider.getHtml())
# print(spider.getHtml())
# spider.xpath_analyzer()
#spider.jsonpath_analyzer()
spider.search()