from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View


# método usando class view
class CarsView(View):

    def get(self, request):
        search = request.GET.get('search')
        # ao passar o order_by se quiser ordenar decrescente é só
        # colocar um '-' antes do nome do campo. Exemplo: order_by('-model')
        if search:
            # busca os dados do banco de dados e salva na variável cars
            cars = Car.objects.filter(
                model__icontains=search).order_by('model')
        else:
            cars = Car.objects.all().order_by('model')

        return render(
            request=request,
            template_name='cars.html',
            context={'cars': cars}
        )


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
