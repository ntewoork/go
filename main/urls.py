from django.urls import path,include
from .views import *
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', Index),
    path('send/',Send),
    path('login/',LoginView.as_view()),
    path('register/',Register),
    path('logout/', Logout),
    path('i18n/en/', include("django.conf.urls.i18n")),
    path('i18n/uz/', include("django.conf.urls.i18n")),
    path('i18n/ru/', include("django.conf.urls.i18n"))

]