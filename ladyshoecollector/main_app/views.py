from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Outfit
from .forms import CleaningForm

# Create your views here.
class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['name', 'shoe_type', 'description']

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    outfits_shoe_doesnt_have = Outfit.objects.exclude(id__in = shoe.outfits.all().values_list('id'))
    cleaning_form = CleaningForm()
    return render(request, 'shoes/detail.html', { 
        'shoe': shoe, 'cleaning_form': cleaning_form, 'outfits': outfits_shoe_doesnt_have
        })

def add_cleaning(request, shoe_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shoe_id = shoe_id
        new_cleaning.save()
    return redirect('detail', shoe_id=shoe_id)


class OutfitList(ListView):
  model = Outfit

class OutfitDetail(DetailView):
  model = Outfit

class OutfitCreate(CreateView):
  model = Outfit
  fields = '__all__'

class OutfitUpdate(UpdateView):
  model = Outfit
  fields = ['top', 'bottom']

class OutfitDelete(DeleteView):
  model = Outfit
  success_url = '/outfits/'

def assoc_outfit(request, shoe_id, outfit_id):
  Shoe.objects.get(id=shoe_id).outfits.add(outfit_id)
  return redirect('detail', shoe_id=shoe_id)