# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

class BrazilianStocks:

    def list_ibovespa_stocks(self):
        url = 'https://br.advfn.com/indice/ibovespa'
        page = requests.get(url)
        stocks = []

        if page.status_code is not 200:
            pass

        parser = BeautifulSoup(page.text, 'html.parser')

        for key, row in enumerate(parser.select('.BovespaIndexListElement table tr')):

            if key == 0:
                continue

            try:
                stocks.append({
                    'name': row.select('.Column1')[0].get_text(),
                    'ticker': row.select('.Column2')[0].get_text(),
                    'url': self.historical_url(row.select('.Column1')[0].find('a')['href'])
                })
            except:
                pass

        return stocks

    def historical_url(self, url):
        return 'https:' + re.sub(r'/cotacao$', '/historico/mais-dados-historicos', url)

    def get_historical(self, ticker):
        pass

    def get_url_from_ticker(self, ticker):
        pass

brs = BrazilianStocks()
print(brs.list_ibovespa_stocks())

