from django.core.management.base import BaseCommand
import requests as rq
from bs4 import BeautifulSoup as bs
import json

class Command(BaseCommand):
    help = 'help text'
    base_url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'
    #base_url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_refresh=19&_paginador_fila_actual=19'

    def handle(self, *args, **options):
        data = {'data':[]}

        number_of_pages = self.getNumberOfPages()
        for i in range(number_of_pages):
            soup = self.getPage(i+1)
            table = self.getTable(soup)
            for item in table:
                item_json = self.getEntryAsJson(item)
                data['data'].append(item_json)
                print(item_json)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

    def getNumberOfPages(self):
        result = rq.get(self.base_url)
        content = result.text
        soup = bs(content,'lxml')
        list_str_number = soup.find(id='info_resultado').get_text().split('\n')[-2].split(': ')[1].split(',')
        return int(''.join(list_str_number))

    def getPage(self, number_of_page_):
        result = rq.get(self.base_url, params={'_paginador_fila_actual':number_of_page_})
        content = result.text
        soup = bs(content,'lxml')
        return soup
    
    def getTable(self, soup):
        return soup.tbody.find_all('tr')

    def getEntryAsJson(self, soup):
        celds = soup.find_all('td')
        result = {}
        result['id'] = int(celds[0].text)
        result['nombre'] = celds[1].find(target='_proyecto').text
        result['tipo'] = celds[2].text
        result['region'] = celds[3].text
        result['tipologia'] = celds[4].text
        result['titular'] = celds[5].text
        result['inversion'] = int(''.join(celds[6].text.split(',')))
        result['fecha'] = celds[7].text
        result['estado'] = celds[8].text

        return result
