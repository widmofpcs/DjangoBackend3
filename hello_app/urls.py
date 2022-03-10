from django.urls import path

from hello_app.views import hello, HelloView

urlpatterns = [
    path('hello/', hello), # ale funkacja bez ()/ Nie wywołujemy jej od razu
    path('', HelloView),
]