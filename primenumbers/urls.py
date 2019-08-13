from django.urls import path

from primenumbers.views import GetPrimeNumbers

urlpatterns = [
    path('', GetPrimeNumbers.as_view(), name="numbers"),
]
