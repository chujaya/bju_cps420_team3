from django.conf.urls import include, url
from django.contrib import admin
import check

urlpatterns = [
    url(r'^check/', include('check.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^main/', check.views.main, name='main'),
]

