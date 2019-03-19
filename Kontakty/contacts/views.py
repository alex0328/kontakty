from django.shortcuts import render
from django.views import View
from contacts import models

# Create your views here.

class MainPageView(View):
    def get(self, request):
        person = models.Person.objects.order_by('name')
        ctx = {'person': person}
        return render(request, 'contacts/index.html', ctx)

class DeleteUserView(View):
    def get(self, request, pk):
        ctx = {}
        return render(request, 'contacts/delete.html', ctx)

class EditUserView(View):
    def get(self, request, pk):
        ctx= {}
        return render(request, 'contacts/edit.html', ctx)

class DetailsUserView(View):
    def get(self, request, pk):
        person = models.Person.objects.filter(id=pk)
        ctx = {'person': person}
        print(ctx)
        return render(request, 'contacts/details.html', ctx)

