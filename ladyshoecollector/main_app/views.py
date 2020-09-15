from django.shortcuts import render
from django.http import HttpResponse

class Shoe:
    def __init__(self, name, shoe_type, description):
        self.name = name
        self.shoe_type = shoe_type
        self.description = description
    
shoes = {
    Shoe('Manolo Blanic', 'stilleto', '6in heel'),
    Shoe('Jessica Simpson', 'wedge', '4in heel'),
    Shoe('Guess', 'high heel', '6in heel'),
}


# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    # shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', { 'shoes': shoes })
