from django.core.management.base import BaseCommand, CommandError
from core.models import MarketData
from core.data import export_details


class Command(BaseCommand):
    help = "clean database and collect data"

    def handle(self, *args, **kwargs):
        MarketData.objects.all().delete()
        res = export_details()
        for i in res:
            one_market = MarketData(
                name=i.get('name'),
                inst=i.get('symbol')
            )
            one_market.save()
        self.stdout.write("Data added successfully")
