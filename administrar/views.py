from django.shortcuts import render
from django.http import HttpResponseRedirect
from administrar.models import Tarea # Importar el modelo
from .forms import TareaForm #para validar

# Create your views here.
def v_index(request):
  if request.method == 'POST':
    ######
    # Post, voy a crear un registro
    ######
    _titulo = request.POST["titulo"]
    
    datos =request.POST.copy()
    
    form = TareaForm(datos) #para validaciones
    if form.is_valid():
      #se pueden hacer validaciones extras con Python
      form.save()
    else:
      # Formulario tiene errores
      return HttpResponseRedirect("/")
    if False:   
       
      tarea = Tarea(datos) # Instancio un modelo
      tarea.titulo = _titulo # Asigno titulo a la tarea
        
      # Antes de *.save, no se guarda nada en en DB
      tarea.save() # Guardo de base de datos
      
    return HttpResponseRedirect("/")
  else:
    # Peticiones method = GET
    consulta = Tarea.objects.filter(titulo__icontains = request.GET.get("titulo", ""))

    #https://lista-tareas.lokcito.repl.co/?estado=1  Filtra a los completados
    #https://lista-tareas.lokcito.repl.co/?estado=0  Filtra a los pendientes
    #https://lista-tareas.lokcito.repl.co/?estado=10000  Filtra a ninguno
    #https://lista-tareas.lokcito.repl.co/?estado=  No Filtra
    #https://lista-tareas.lokcito.repl.co/  No filtra
    #https://lista-tareas.lokcito.repl.co/?titulo=Bailar No filtra
    
    if request.GET.get("estado", "") != "":
      consulta = consulta.filter(estado = request.GET.get("estado", ""))
      
    ## Listar las tareas
    context = {
      'var1': 'Valor1',
      'var2': 'Valorasdasdasdasdasd',
      'lista': consulta
    }
    return render(request, 'pagina_x.html', context)

def v_eliminar(request, tarea_id):
  Tarea.objects.filter(id = tarea_id).delete()
  return HttpResponseRedirect("/") # Redirigir

def v_completado(request, tarea_id):
  task = Tarea.objects.get(id = tarea_id)
  task.estado = 1
  task.save()
  return HttpResponseRedirect('/')