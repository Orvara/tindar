from django.conf.urls import url
from . import views

app_name = 'tindarapp'

urlpatterns = [
    url(r'^about/$',views.AboutPage,name='about'),
    url(r'^pantanir/$',views.PantanirPage,name='pantanir'),
]
