import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Notes
# Create your views here.


class NotesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, req, *args, **kwargs):
        return super().dispatch(req, *args, **kwargs)

    def get(self, req, id=0):
        if(id > 0):
            notes = list(Notes.objects.filter(id=id).values())
            if len(notes) > 0:
                note = notes[0]
                datos = {'message': 'success', 'note': note}
            else:
                datos = {'message': "Not found..."}
            return JsonResponse(datos)
        else:
            notes_list = list(Notes.objects.values())
            if len(notes_list) > 0:
                datos = {'message': 'success', 'notes': notes_list}
            else:
                datos = {'message': 'Not found...'}
            return JsonResponse(datos)

    def post(self, req):
        jd = json.loads(req.body)
        # print(jd)
        Notes.objects.create(title=jd['title'], text=jd['text'])
        datos = {'message': 'success'}
        return JsonResponse(datos)

    def put(self, req, id):
        jd = json.loads(req.body)
        notes = list(Notes.objects.filter(id=id).values())
        if len(notes) > 0:
            note = Notes.objects.get(id=id)
            note.title = jd['title']
            note.text = jd['text']
            note.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Not found...'}
        return JsonResponse(datos)

    def delete(self, req, id):
        notes = list(Notes.objects.filter(id=id).values())
        if len(notes) > 0:
            Notes.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Not found...'}
        return JsonResponse(datos)


