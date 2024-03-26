
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path ('', include('expenses.urls')),
    path ('authentication/', include('authentication.urls')),
    path ('preferences/', include('preferences.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'))
]



