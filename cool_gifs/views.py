from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Image


class PermaLinkView(DetailView):
    model = Image
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = HttpResponse(content_type=self.object.content_type)
        response['X-Accel-Redirect'] = self.object.src.url
        return response


