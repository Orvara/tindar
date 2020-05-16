from django.conf.urls import url
from . import views

app_name = 'tindarapp'

urlpatterns = [
    url(r'^about/$',views.AboutPage,name='about'),
    url(r'^pantanir/$',views.form_name_view,name='form_name_view'),
    url(r'^myndaalbum/$',views.MyndirPage,name='myndir'),
]
