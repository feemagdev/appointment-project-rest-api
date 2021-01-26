from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register('bclient', views.BusinessClientViewSet, base_name="bclient")
router.register('client', views.ClientViewSet, base_name="client")
router.register('employee', views.EmployeeViewSet, base_name="employee")
router.register('pappointment', views.PersonalAppointmentViewSet,
                base_name="pappointment")
router.register('bappointment', views.BusinessAppointmentViewSet,
                base_name="bappointment")
router.register('company', views.CompanyViewSet, base_name="company")

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
