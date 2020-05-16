from django.conf.urls import url
from . import views

app_name = 'tindarapp'

urlpatterns = [
    url(r'^about/$',views.AboutPage,name='about'),
    url(r'^pantanir/$',views.showform,name='form_name_view'),
    url(r'^myndaalbum/$',views.MyndirPage,name='myndir'),
    url(r'^thanks/$',views.thanks,name='thanks'),
]
