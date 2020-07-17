from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home

handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('',include('core.urls',namespace='core'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)