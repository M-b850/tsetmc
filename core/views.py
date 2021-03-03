from django.shortcuts import render
from . import data
from core.models import MarketData


def get_data(request):
    res = data.export_details()
    for i in res:
        one_market = MarketData(
            name=i.get('name'),
            inst=i.get('symbol')
        )
        one_market.save()
        all_data = MarketData.objects.all()
    
    return render(request, 'home.html', {"all_data": all_data})
