
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    # path('', include(apps.get_app_config('oscar').urls[0])),
]
