import datetime
# from random import randint
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.contrib.messages.views import SuccessMessageMixin
# from django.core.mail import send_mail, EmailMessage
# from django.http import HttpResponse
from django.shortcuts import redirect
# from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
# from LimitlessProject.settings import EMAIL_HOST_USER
from home.forms import UserForm, FlightUpdateForm, FlightCreateForm, AircraftCreateForm, ContactCreateForm, \
	OperatorUpdateForm
# from home.functions import handle_uploaded_file
# from home.forms import UserForm, FlightFilters
from home.models import FlightLog, Aircraft, Operator, Contact


class HomeTemplateView(TemplateView):
	template_name = 'home/homepage.html'


class ProfileTemplateView(TemplateView):
	template_name = 'home/user_profile.html'


class UserCreateView(CreateView):
	template_name = 'home/create_user.html'
	model = Operator
	form_class = UserForm
	success_url = reverse_lazy('homepage')

	def form_valid(self, form):
		if form.is_valid():
			new_user = form.save(commit=False)  # salvam datele in tabelul auth_user
			new_user.first_name = new_user.first_name.title()
			new_user.last_name = new_user.last_name.title()
		# new_user.username =
		# f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{randint(100000, 999999)}'
		# new_user.save()
		#
		# details_user = {
		# 	'fullname': f'{new_user.first_name} {new_user.last_name}',
		# 	'username': new_user.username
		# }
		# subject = "Confirmare cont nou in Limitless FPV"
		# message = get_template('mail.html').render(details_user)
		# mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
		# mail.content_subtype = 'html'
		# mail.send()

		return super().form_valid(form)


class FlightListView(LoginRequiredMixin, ListView):
	template_name = 'home/list_of_flights.html'
	model = FlightLog
	context_object_name = "all_flights"
	success_message = 'Flight log has been added'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		now = datetime.datetime.now()
		context['current_date'] = now
		return context

	def get_queryset(self):
		return FlightLog.objects.filter(operator=self.request.user)


# Search
# get_all_flights = FlightLog.objects.filter(active=True)
# my_filters = FlightFilters(self.request.GET, queryset=get_all_flights)
# get_all_flights = my_filters.qs
# context['all_flights'] = get_all_flights
# context['form_filters'] = my_filters.form


class FlightDetailView(LoginRequiredMixin, DetailView):
	template_name = 'home/flight_details.html'
	model = FlightLog


class FlightUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'home/update_flight.html'
	model = FlightLog
	form_class = FlightUpdateForm
	success_url = reverse_lazy('list-of-flights')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		form = context['form']
		form.fields['aircraft'].queryset = Aircraft.objects.filter(owner=self.request.user)
		context['form'] = form
		return context

	def form_valid(self, form):
		if form.is_valid():
			log = form.save(commit=False)
			log.operator = self.request.user
			log.save()
			return redirect(self.success_url)


class FlightDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'home/delete_flight.html'
	model = FlightLog
	success_url = reverse_lazy('list-of-flights')


class MyZoneView(TemplateView):
	template_name = 'home/my_zone.html'


class FlightCreateView(LoginRequiredMixin, CreateView):
	template_name = 'home/flight_add.html'
	model = FlightLog
	form_class = FlightCreateForm
	success_url = reverse_lazy('list-of-flights')

	def form_valid(self, form):
		if form.is_valid():
			log = form.save(commit=False)
			log.operator = self.request.user
			log.save()
			return redirect(self.success_url)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		form: FlightCreateForm = context['form']
		form.fields['aircraft'].queryset = Aircraft.objects.filter(owner=self.request.user)
		context['form'] = form
		return context


class AircraftCreateView(LoginRequiredMixin, CreateView):
	template_name = 'home/add_aircraft.html'
	model = Aircraft
	form_class = AircraftCreateForm
	success_url = reverse_lazy('flight-add')

	def form_valid(self, form):
		if form.is_valid():
			log = form.save(commit=False)
			log.owner = self.request.user
			log.save()
			return redirect(self.success_url)


class ContactCreateView(CreateView):
	template_name = 'home/contact.html'
	model = Contact
	form_class = ContactCreateForm
	success_url = reverse_lazy('homepage')


class OperatorUpdateView(UpdateView):
	template_name = 'home/certificate_upload.html'
	model = Operator
	form_class = OperatorUpdateForm
	success_url = reverse_lazy('user_profile')


# class PassResetView(UpdateView):
# 	template_name = 'registration/password_reset_form.html'
# 	model = Operator
# 	form_class = PasswordResetForm
# 	success_url = reverse_lazy('homepage')
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		form = context['form']
# 		form.fields['email'].queryset = Aircraft.objects.filter(owner=self.request.user)
# 		context['form'] = form
# 		return context
