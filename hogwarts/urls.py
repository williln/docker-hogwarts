from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('spells/', include('spells.urls')),
    path('admin/', admin.site.urls),
]
