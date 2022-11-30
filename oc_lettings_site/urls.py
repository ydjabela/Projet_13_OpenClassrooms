from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls", namespace='homes')),
    path('lettings/', include("letting.urls", namespace='lettings')),
    path('profiles/', include("profiles.urls", namespace='profiles')),


]
