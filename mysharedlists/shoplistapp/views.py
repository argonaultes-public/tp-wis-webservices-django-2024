from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Store

# Create your views here.
# DRY Don't Repeat Yourself
# Convention Over Configuration
def index(request):
    stores = Store.objects.all()
    template = loader.get_template('index.html')
    context = {'stores': stores}
    return HttpResponse(template.render(context, request))

def index_json(request):
    stores = Store.objects.all()
    stores_json = [ {'store_name': store.store_name} for store in stores]
    return JsonResponse(data = stores_json, safe=False)
