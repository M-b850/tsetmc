from django.test import TestCase

from core.models import MarketData
from core.data import export_details

from scraping.task import AddData


class DataTest(TestCase):
    """Collect and crawl Data"""
    def test_add_to_database(self):
        market = export_details()
        name = market[50].get('name')
        a = MarketData.objects.create(
            name=market[50].get('name'),
            inst=market[50].get('symbol')
        )
        self.assertEquals(a.name, name)

    def test_data_works(self):
        a = AddData()
        a.create_objects()
        self.assertEquals(
            len(MarketData.objects.all()),
            len(export_details())
            )   
    