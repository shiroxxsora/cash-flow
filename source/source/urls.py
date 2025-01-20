from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from cashflow.views import StatusViewSet, TypeViewSet, CategoryViewSet, UndercatViewSet, CashflowViewSet, UndercatListViewSet


router = DefaultRouter()
router.register(r'statuses', StatusViewSet)
router.register(r'types', TypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'undercats', UndercatViewSet)
router.register(r'cashflows', CashflowViewSet)
router.register(r'undercat-lists', UndercatListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
    path('edit-page', TemplateView.as_view(template_name='edit-page.html'))
]