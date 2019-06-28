from django.views.generic import DetailView, ListView

from .models import Image


class Index(ListView):

    model = Image


class Detail(DetailView):
    model = Image
