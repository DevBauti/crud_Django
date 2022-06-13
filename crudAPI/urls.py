from django.urls import path
from .views import NotesView


# esto inicializa las rutas
urlpatterns = [
    path('notes/', NotesView.as_view(), name='notes_list'),
    path('notes/<int:id>', NotesView.as_view(), name='notes_process')

]