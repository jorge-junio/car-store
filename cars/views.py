from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


# esta forma é muito trabalhosa, deixamos de usar esta classe
def cars_view(request):
    search = request.GET.get('search')
    # ao passar o order_by se quiser ordenar decrescente é só
    # colocar um '-' antes do nome do campo. Exemplo: order_by('-model')
    if search:
        # busca os dados do banco de dados e salva na variável cars
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request=request,
        template_name='new_car.html',
        context={'new_car_form': new_car_form}
    )
