from django.shortcuts import render, redirect
from .forms import PersonaModelForm
from .models import Persona


def persona_list(request):
    context = {'persona_list': Persona.objects.all()}
    return render(request, "datos/list.html", context)

def persona_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PersonaModelForm()
        else:
            persona = Persona.objects.get(pk=id)
            form = PersonaModelForm(instance=persona)
        return render(request, "datos/main.html", {'form': form})
    else:
        if id == 0:
            form = PersonaModelForm(request.POST)
        else:
            persona = Persona.objects.get(pk=id)
            form = PersonaModelForm(request.POST,instance= persona)
        if form.is_valid():
            form.save()
        return redirect('/datos/add/')

def persona_delete(request, id=0):
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect('/datos/add/')


