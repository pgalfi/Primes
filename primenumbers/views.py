import json

from django import views
from django.http import HttpResponse

from primenumbers.services.primes import get_primes


class GetPrimeNumbers(views.generic.TemplateView):

    def get(self, request, *args, **kwargs):
        page_size = int(request.GET.get("page_size", 100))
        page = int(request.GET.get("page", 1))
        start = int(request.GET.get("start", 1))
        n = int(request.GET.get("n", 1))
        results = get_primes(n, start=start, page=page, size=page_size)
        return HttpResponse(json.dumps(results))
