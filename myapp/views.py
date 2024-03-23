from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.http import JsonResponse
# Create your views here.
def home(request):
    product = Image.objects.all()
    context = {"products":product}
    return render(request,"index.html",context)

def getData(request):
    objects = Image.objects.all()
    context = {
        "products": [],
    }
    for obj in objects:
        tmp = {
            "url": obj.photo.url,
            "name": obj.name,
            "price": obj.price,
        }
        context['products'].append(tmp)
    print(context)
    # return HttpResponse("ok")
    return JsonResponse(context)