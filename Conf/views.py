from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from jsonschema import validate
import json
from .models import Save_File

schema_exp = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "status": {"type": "string"},
    },
}


def valid_file(json_data):
    try:
        validate(instance=json_data, schema=schema_exp)
    except Exception:
        raise Http404("Не соответствует json schema")
    return True


def list(request):
    list_file = Save_File.objects.all()
    return render(request, 'Files/list.html', {'list_file': list_file})


def data(request, file_id):
    f = Save_File.objects.get(id=file_id).save_file
    f.open(mode='r')
    lines = f.readlines()
    f.close()
    return render(request, 'Files/data.html', {'text': lines})


def list2(request):
    list_file = Save_File.objects.all()
    return render(request, 'Files/list2.html', {'list_file': list_file})


def edit(request, file_id):
    f = Save_File.objects.get(id=file_id).save_file
    f.open(mode='r')
    lines = f.readlines()
    f.close()
    obj = Save_File.objects.get(id=file_id)
    return render(request, 'Files/edit.html', {'text': lines, 'obj': obj})


def save_edit(request, file_id):
    try:
        json_data = request.POST['text']
        json_data = json.loads(json_data)
    except Exception:
        raise Http404("Неверный формат")
    res = valid_file(json_data)
    if res:
        f = Save_File.objects.get(id=file_id).save_file
        f.open(mode='w')
        f.write(f'{request.POST["text"]}')
        f.close()
        return HttpResponseRedirect('http://127.0.0.1:8000')
    else:
        raise Http404("Неверный формат")


def new(request):
    return render(request, 'Files/new_file.html')


def new_save(request):
    try:
        json_data = request.POST['text']
        json_data = json.loads(json_data)
    except:
        raise Http404("Неверный формат")
    res = valid_file(json_data)
    if res:
        f = open(f'media/{request.POST["name"]}.json', mode="w")
        f.write(request.POST['text'])
        f.close()
        Save_File.objects.create(save_file=f'{request.POST["name"]}.json')
        return HttpResponseRedirect('http://127.0.0.1:8000')
