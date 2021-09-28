from requests_html import HTMLSession
import json

test_url = "https://www.900gpa.com/en/search"


params = {
    'p': 'resin',
    'u': 'metric',
    'refinements%5BproductInformation.matrixType%5D%5B0%5D': 'Thermoset',
    'refinements%5BproductInformation.resinType%5D%5B0%5D': 'BMI',
    'uid': 'ResinPreg_00D763EF0C'
}


def get_request(url):
    session = HTMLSession()
    res = session.get(url, params=params)
    try:
        res.raise_for_status()
    except ValueError as e:
        raise('Dead link')
    res.html.render(sleep=2, timeout=20)
    return res


def get_material_info(t):
    response = {}
    table_rows = t.find('tr')
    for tr in table_rows:
        if tr.find('strong', first=True) is not None:
            key = tr.find('strong', first=True).text
            response[key] = tr.find('td', first=True).text
    return response


def start_scraping(res):
    response = {}
    tables = res.html.find('table')
    for table in tables:
        key = table.find('h4', first=True).text
        response[key] = get_material_info(table)
    return response


res = get_request(test_url)
data = start_scraping(res)
# print(json.dumps(data, indent=4, sort_keys=True))


with open("data.txt", "w") as external_file:
    data = start_scraping(res)
    print(data, file=external_file)
    external_file.close()
