from django.shortcuts import render
from .models import Notice
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getnotice(request):
    qset=Notice.objects.all().order_by('position')
    data=json.loads(serialize('json', qset))
    return JsonResponse({"data":data})

# Create your views here.
