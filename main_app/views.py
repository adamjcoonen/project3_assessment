from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Widget

# Create your views here.

def index(request):
    widgets_list = Widget.objects.all()
    return render(request, 'index.html', {'widgets_list' : widgets_list})



class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'


def delete_widget(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('index')