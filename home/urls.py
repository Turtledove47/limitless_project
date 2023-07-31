from django.urls import path
from home import views


urlpatterns = [
	path('', views.HomeTemplateView.as_view(), name='homepage'),
	path('MyZone/create_operator/', views.UserCreateView.as_view(), name='create-user'),
	path('MyZone/', views.MyZoneView.as_view(), name='my-zone'),
	path('MyZone/flight_list/', views.FlightListView.as_view(), name='list-of-flights'),
	path('MyZone/flight_details/<int:pk>', views.FlightDetailView.as_view(), name='flight-details'),
	path('MyZone/update_flight/<int:pk>/', views.FlightUpdateView.as_view(), name='update-flight'),
	path('MyZone/delete_flight/<int:pk>/', views.FlightDeleteView.as_view(), name='delete-flight'),
	path('MyZone/profile/', views.ProfileTemplateView.as_view(), name='user_profile'),
	path('MyZone/add_flight/', views.FlightCreateView.as_view(), name='flight-add'),
	path('MyZone/add_aircraft/', views.AircraftCreateView.as_view(), name='aircraft-add'),
	path('contact_form/', views.ContactCreateView.as_view(), name='contact'),
	path('MyZone/add_certificates/<int:pk>', views.OperatorUpdateView.as_view(), name='certificates-add'),
	path('password_reset/', views.PassResetView.as_view(), name='password-reset'),
]
