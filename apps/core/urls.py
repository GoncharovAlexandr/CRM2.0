from django.urls import path
from apps.core import views as core_views
from django.urls import path, re_path
urlpatterns = [
    path('', core_views.main),
]