from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dob_rest_api import views
router = DefaultRouter()

router.register('profile',views.UserProfileViewSet,basename='profile')
urlpatterns=[

    path('',include(router.urls))
]
