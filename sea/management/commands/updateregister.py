from django.core.management.base import BaseCommand
import json
from sea.models import SEIA

class Command(BaseCommand):

    def handle(self, *args, **options):
        data = {}
        obj = dict()
        with open('data.json') as file:
            data = json.load(file)
        for item in data['data']:
            #id = item.pop('id')
            item['fecha'] = '-'.join(list(reversed(item['fecha'].split('/'))))
            obj[item["id"]]=SEIA(**item)
        created = set(SEIA.objects.filter(id__in=obj.keys()).values_list("id", flat=True))
        cobj = dict()
        for id in created:
            cobj[id] = obj.pop(id)
        SEIA.objects.bulk_create(obj.values())
        SEIA.objects.bulk_update(cobj.values(), fields=[f for f in item.keys() if f != "id"])
        
