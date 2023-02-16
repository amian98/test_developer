import requests as rq
from django.core.management.base import BaseCommand, CommandError
from bike.models import *

class Command(BaseCommand):
    help = 'help text'

    base_url = 'http://api.citybik.es/v2/networks/bikesantiago'

    def handle(self, *args, **options):
        response = self.get_request()
        if response == '':
            return
        else:
            for item in response:
                item_extra = item.pop('extra')
                item_payment = item_extra.pop('payment')
                station = self.create_station(item)
                self.create_extra(item_extra, station)
                self.create_payment(item_payment, station)


    def get_request(self):
        response = rq.get(self.base_url)
        if response.status_code != 200:
            self.stderr("Status code: "+ str(response.status_code))
            return ''
        else:
            return response.json()['network']['stations']

    def create_station(self, response):
        id = response.pop('id')

        station, _ = Station.objects.update_or_create(id=id, defaults=response)
        return station

    def create_extra(self, response, station_):
        response['payment_terminal'] = response.pop('payment-terminal')
        extra, _ = Extra.objects.update_or_create(station=station_, defaults=response)
        return extra

    def create_payment(self, response, station_):
        for index, value in enumerate(response):
            Payment.objects.update_or_create(station=station_, payment_method=response[index])
