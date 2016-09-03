from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^weblog/$', views.WidthEntryIndex.as_view(), name='width_entry_index'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]
