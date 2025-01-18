from cashflow.views import CashflowAPIView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/cashflowlist/', CashflowAPIView.as_view())
]
