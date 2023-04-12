from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('placementStories.urls')),
    path('users/',include('users.urls')),
    path('chat/', include('chat.urls')),
    path('events/',include('events.urls')),
    path("classroom/", include('classroom.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)