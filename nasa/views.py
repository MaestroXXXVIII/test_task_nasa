from django.shortcuts import render
from .models import Slider

def slider_list(request):
    images = Slider.objects.all()
    return render(request, 'base.html', {'images': images})