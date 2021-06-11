from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noughtpad_app.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('authpad_app.urls'))
]
