from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from musics.views import MusicViewSet

router = routers.DefaultRouter()
router.register('musics', MusicViewSet) # prefix = musics이고 viewset = MusicViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]