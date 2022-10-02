import requests
import json
from multiprocessing import Pool
import urllib.request

SIZE_LIMIT = 5000000
counter = 0


def download(url):
    if check_file_size(url) <= SIZE_LIMIT:
        urllib.request.urlretrieve(url, "./dataset/" + url.split('/')[-1])


def check_file_size(url):
    f = requests.head(url)
    if f.status_code != 200:
        return SIZE_LIMIT + 1
    return int(f.headers['Content-Length'])


def json_post(url, json_dictionary):
    r = requests.post(url, json=json_dictionary)
    if r.status_code != 200:
        return {}
    return json.loads(r.text)


if __name__ == '__main__':
    downloads = set()
    print("Enter Download Query Range")
    a = int(input())
    b = int(input())
    for page in range(a,b):
        search_term = {
            "disseminated": "DOCUMENT_AND_METADATA",
            "distribution": "PUBLIC",
            "sort": {
                "field": "published",
                "order": "desc"
            },
            "page": {
                "size": 100,
                "from": page
            }
        }
        res = json_post('https://ntrs.nasa.gov/api/citations/search', search_term)
        res = res['results']
        print(page)

        for i in res:
            if 'keywords' not in i:
                continue

            if 'downloads' in i:
                for d in i['downloads']:
                    if 'pdf' in d['links']:
                        link = 'https://ntrs.nasa.gov' + d['links']['pdf']
                        downloads.add(link)
                        with open(f'./dataset/{link.split("/")[-1]}.txt', 'w') as f:
                            for k in i['keywords']:
                                f.write(f'{k},')

    p = Pool()
    p.map(download, list(downloads))
    p.close()
    p.join()
