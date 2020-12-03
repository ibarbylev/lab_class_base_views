from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View, TemplateView

from cbv.models import PetForExample


class IndexView(View):
    def get(self, request):
        context = {'heading_text': 'Hello from View!', 'pets': PetForExample.objects.all()}
        return render(request, 'cbv/index.html', context)

    def post(self, request):
        pass


class IndexTemplateView(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        return {'heading_text': 'Hello from Template View!', 'pets': PetForExample.objects.all()}


class PetForExampleListView(ListView):
    template_name = 'cbv/index.html'
    model = PetForExample
    context_object_name = 'pets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Pets list'

        return context


class PetForExampleDetailsView(DetailView):
    template_name = 'cbv/details.html'
    model = PetForExample
    context_object_name = 'pet'  # !!! not 'pets', but only 'pet' !!!!1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']
        context['heading_text'] = f'{pet}\'s details'

        return context


class PetForExampleCreateView(CreateView):
    model = PetForExample
    template_name = 'cbv/create-pet.html'
    fields = '__all__'
    success_url = reverse_lazy('cbv_index list')

