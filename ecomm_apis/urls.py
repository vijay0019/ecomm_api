from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('/', )
    path('api/', include('ecomm_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
