
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello-api/', views.HelloApiView.as_view()),
]
