from django.conf.urls import include, url
from django.contrib import admin
import check
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^check/', include('check.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^main/', check.views.main, name='main'),
    url(r'^home/', check.views.home, name="home"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

