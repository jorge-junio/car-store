from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView


# usando ListView
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        # ao passar o order_by se quiser ordenar decrescente é só
        # colocar um '-' antes do nome do campo. Exemplo: order_by('-model')
        if search:
            # busca os dados do banco de dados e salva na variável cars
            cars = cars.filter(model__icontains=search)
        return cars


# método usando class view
class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request=request, template_name='new_car.html',
            context={'new_car_form': new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(
            request=request, template_name='new_car.html',
            context={'new_car_form': new_car_form})
