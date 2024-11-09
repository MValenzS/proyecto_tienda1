from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Oferta
from .forms import OfertaForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required()
@permission_required('ofertas.editar_oferta', raise_exception=True)
def editar_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id)
    if request.method == 'POST':
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form = OfertaForm(instance=oferta)
    return render(request, 'ofertas/crear_oferta.html', {'form': form})

@permission_required('ofertas.eliminar_oferta', raise_exception=True)
def eliminar_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id)
    if request.method == 'POST':
        oferta.delete()
        return redirect('ofertas: index')
    return render(request, 'ofertas/eliminar_oferta.html', {'oferta': oferta})

@permission_required('oferta.crear_oferta', raise_exception=True)
def crear_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ofertas:index')
    else:
        form = OfertaForm
    return render(request, 'ofertas/crear_oferta.html', {'form': form})

def index(request):
    current_date = datetime.now()
    ofertas = []

    try:
        ofertas = Oferta.objects.filter(fecha_inicio__lte=current_date,
                                        fecha_fin__gte=current_date)
        # raise Exception("no hay ofertas disponibles en este momento")
        if not ofertas:
            raise ValueError("no hay ofertas disponibles en este momento")
    except ValueError as e:
        # manejo de error especifico
        return render(request, 'ofertas/index.html', {'error': str(e),
                                                      'current_date': current_date})
    except Exception as e:
        # Manejo de cualquier otro error
        return render(request, 'ofertas/index.html',
                      {'error': 'Se produjo  un error inesperado!', 'current_date': current_date})
    context = {
        'current_date': current_date,
        # is_special_offer: False #false para no y true para si
        'ofertas': ofertas
    }
    return render(request, 'ofertas/index.html', context)
