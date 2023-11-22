from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/', views.home, name='home'),
    path('login', views.login_view, name='login_view'),
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('consultar', views.consultar, name='consultar'),
    path('save', views.save, name='save'),
    path('signout', views.signout, name='signout'),
    
]
