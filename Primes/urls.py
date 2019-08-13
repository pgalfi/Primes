from django.urls import include, path

urlpatterns = [
    path("primenumbers/", include('primenumbers.urls'))
]
