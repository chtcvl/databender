from django.shortcuts import render
from django.http import HttpResponse

dsn = "hostaddr=127.0.0.1 port=5432 dbname=INTEGRATIONS user=postgres password=postgres"
query = "select * from public.sources"


def index(request):
    return render(request, 'base.html')
