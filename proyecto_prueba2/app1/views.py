from django.shortcuts import render_to_response 
from django.template import RequestContext
from app1.models import Alumno


def inicio(request):
    detalle="Pagina de Inicio"
    alumnos = Alumno.objects.all()
    
    return render_to_response('inicio.html',
                              {'detalle':detalle,
                               'alumnos':alumnos},
                              context_instance=RequestContext(request)
                              )
    
    
def alumno_lista(request):
    alumnos = Alumno.objects.all()
    detalle="Lista de Alumnos"
    return render_to_response('alumno_lista.html',
                              {
                               'alumnos':alumnos,
                               'detalle':detalle
                              },
                              context_instance=RequestContext(request)
                              )
    

