from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
import pandas as pd


class Home(TemplateView):
    template_name = 'upload.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)

        file_path = '/media/' + name
        context['url'] = file_path

        # target_locations = pd.read_csv(file_path)
        # context['url'] = target_locations

    return render(request, 'upload.html', context)
