from django.http import JsonResponse, Http404
from shop.models import *
import json


def imports(request):
    if request.method == 'POST':
        citizens = json.loads(request.body)['citizens']
        im = Import.objects.create()
        for d in citizens:
            cit = Citizen(**d)
            cit.save()
            im.citizens.add(cit)
            im.save()
        return JsonResponse({"data": {"import_id": im.id}}, status=201)
    else:
        raise Http404
