from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from shop.models import *
import json


@require_http_methods(["POST"])
def imports(request):
    try:
        citizens = json.loads(request.body)['citizens']
        im = Import.objects.create()
        for man in citizens:
            new_citizen = Citizen.objects.create(
                citizen_id=man['citizen_id'], town=man['town'], street=man['street'], building=man['building'],
                apartment=man['apartment'], name=man['name'], birth_date=man['birth_date'], gender=man['gender']
            )
            new_citizen.save()
            im.citizens.add(new_citizen)
        for d in citizens:
            current = im.citizens.get(citizen_id=d['citizen_id'])
            print(current)
            for rel in d['relatives']:
                print(rel)
                r = im.citizens.get(citizen_id=rel)
                current.relatives.add(r)
            current.save()
        im.save()
    except:
        return HttpResponseBadRequest()
    return JsonResponse({"data": {"import_id": im.id}}, status=201)


@require_http_methods(["PATCH"])
def change(request, import_id, citizen_id):
    changes_data = json.loads(request.body)
    im = Import.objects.get(import_id=import_id)
    current = im.citizens.get(citizen_id=citizen_id)
    for key in changes_data.keys():
        current
    return HttpResponseBadRequest('Все плохо')


@require_http_methods(["GET"])
def get_citizens(request, import_id):
    try:
        all_citizens = Import.objects.get(id=import_id).citizens.all()
        sum_list = []
        for man in all_citizens:
            dict_obj = model_to_dict(man)
            del dict_obj['id']
            rel = man.relatives.all()
            dict_obj['relatives'].clear()
            for r in rel:
                dict_obj['relatives'].append(r.citizen_id)
            sum_list.append(dict_obj)
    except:
        return HttpResponseBadRequest()
    return JsonResponse({'data': sum_list}, status=200)