from django.shortcuts import render
from django.views.generic import CreateView
from .models import Widget

# Create your views here.

def index(request):
    widgets_list = Widget.objects.all()
    return render(request, 'index.html', {'widgets_list' : widgets_list})



class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'