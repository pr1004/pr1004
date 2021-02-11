
from django.urls import path, include
from . import views
from django.conf import settings
urlpatterns = [
  path('', views.index, name='index')
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns += path(r'^__debug__/', include(debug_toolbar.urls)),