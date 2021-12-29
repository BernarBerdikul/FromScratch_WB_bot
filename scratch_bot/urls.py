from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("scratch_admin/", admin.site.urls),
]
