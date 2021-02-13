from django.urls import path, include
from . import views
from django.conf import settings
urlpatterns = [
  path('sign_up/', views.sign_up, name='sign_up'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns += path(r'^__debug__/', include(debug_toolbar.urls)),