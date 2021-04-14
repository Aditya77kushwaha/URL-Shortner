from django.shortcuts import render, redirect
import uuid
from .models import MyModel
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = MyModel(link=link, unique_id=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = MyModel.objects.get(unique_id=pk)
    return redirect(url_details.link)
