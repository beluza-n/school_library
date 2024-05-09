from django.shortcuts import render
from .models import Asset


def asset_list(request):
    assets = Asset.objects.all()

    template = 'asset_list.html'
    context = {'assets': assets}
    return render(request, template, context)