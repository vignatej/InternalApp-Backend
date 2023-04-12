from .views import createUser, getUserDeatils, getProfiles
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user/',createUser,name="createUser"),
    path('getDetails/',getUserDeatils, name="getuserdetails"),
    path('getAllProfiles/',getProfiles, name="getAllProfiles")
]
