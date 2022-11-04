from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SongViewSet

router =DefaultRouter()
router.register('songs', SongViewSet, basename='songs')

urlpatterns = [
    path('songs', SongViewSet.as_view({
        'get': 'list'
    }), name='song_list'),
    path('song/<int:pk>', SongViewSet.as_view ({
        'get':'retrieve', 'patch',:'update', 'delete': 'destroy'
    }), name='song-detail')
]

127.0.0:8000/api