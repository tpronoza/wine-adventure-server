from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from wineadventureapi.views import register_user, check_user, WineView, Wine101View, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'wines', WineView, 'wine')
router.register(r'wines101', Wine101View, 'wine101')
router.register(r'categories', CategoryView, 'category')
# router.register(r'profiles', ProfileView, 'profile')
# router.register(r'users', UserView, 'user')
# router.register(r'wineries', WineryView, 'winery')
# router.register(r'countries', CountryView, 'country')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]
