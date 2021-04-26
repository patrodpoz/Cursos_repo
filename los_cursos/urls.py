from django.urls import path, include
from . import views  
urlpatterns = [
    path('', views.cursos),
    path('agregar_curso', views.agregar_curso),
    path('curso/destroy/<int:idCurso>', views.eliminar_curso),
    path('eliminar/<int:idCurso>', views.eliminar),




]