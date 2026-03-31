from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView


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


# usando CreateView
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
