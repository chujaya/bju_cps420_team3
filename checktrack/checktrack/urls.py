from django.conf.urls import include, url
from django.contrib import admin
import check
from django.conf import settings
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views
>>>>>>> 0cff3080d2f9aeba8b17c0a40fc7549e31141a90
from django.conf.urls.static import static


urlpatterns = [
    url(r'^check/', include('check.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^main/', check.views.main, name='main'),
<<<<<<< HEAD
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^home/', check.views.home, name="home"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

>>>>>>> 0cff3080d2f9aeba8b17c0a40fc7549e31141a90
