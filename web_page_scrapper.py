from requests_html import HTMLSession

test_url = "https://www.900gpa.com/en/search"
params = {
    'p': 'resin',
    'u': 'metric',
    'refinements%5BproductInformation.matrixType%5D%5B0%5D': 'Thermoset',
    'refinements%5BproductInformation.resinType%5D%5B0%5D': 'BMI'
}


class WebScrapper:

    def __init__(self):
        self.params = params
        self.session = HTMLSession()
        self.url = test_url

    def request_data(self, id):
        print("Requesting data for uid: ", id, "...")
        self.params['uid'] = id
        response = self.session.get(self.url, params=self.params)
        try:
            response.raise_for_status()
        except ValueError as e:
            raise "Dead link"
        response.html.render(sleep=2, timeout=20)
        data = {}
        tables = response.html.find('table')
        for table in tables:
            key = table.find('h4', first=True).text
            data[key] = self.get_material_info(table)
        return data

    @staticmethod
    def get_material_info(t):
        response = {}
        table_rows = t.find('tr')
        for tr in table_rows:
            if tr.find('strong', first=True) is not None:
                key = tr.find('strong', first=True).text
                response[key] = tr.find('td', first=True).text
        return response
