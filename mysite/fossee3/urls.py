from django.conf.urls import url
from fossee3 import views
app_name = "fossee3"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadDocument$', views.uploadDocument, name='uploadDocument'),
    url(r'^viewDocument$', views.viewDocument, name='viewDocument'),

]