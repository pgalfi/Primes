import json

from django import views
from django.http import HttpResponse

from primenumbers.forms import GetPrimeNumbersParamsForm
from primenumbers.services.primes import get_primes


class GetPrimeNumbers(views.generic.TemplateView):

    def get(self, request, *args, **kwargs):
        params = GetPrimeNumbersParamsForm(data=request.GET)
        if params.is_valid():
            results = get_primes(params.cleaned_data["n"], start=params.cleaned_data["start"],
                                 page=params.cleaned_data["page"], size=params.cleaned_data["page_size"])
            return HttpResponse(json.dumps(results))
        return HttpResponse(json.dumps({"errors": params.errors}))
