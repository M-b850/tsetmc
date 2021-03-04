from django.shortcuts import render
from core.models import MarketData


def get_data(request):

    all_data = MarketData.objects.all()
    return render(request, 'home.html', {"all_data": all_data})
