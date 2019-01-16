from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.location, name='location'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^neighbourhood/(\d+)', views.neighbourhood, name='neighbourhood'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^update_profile/(\d+)$', views.update_profile, name='update_profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^add_business/', views.add_business, name='add_business'),
    url(r'^change_neighbourhood/(\d+)', views.change_neighbourhood, name='change_neighbourhood'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
