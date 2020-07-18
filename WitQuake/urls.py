
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf.urls.static import static
from WitQuake import settings
# from community import views
from django.views.generic.base import RedirectView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('learn.urls')),
    path('forum/', include('community.urls')),
    path('accounts/', include('registration.backends.default.urls')),  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
