from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
