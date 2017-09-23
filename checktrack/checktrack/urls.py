from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^check/', include('check.urls')),
    url(r'^admin/', admin.site.urls),
]

