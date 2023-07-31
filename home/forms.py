from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
# from django.contrib.auth.models import User
# from django.contrib.auth.views import PasswordChangeView
# import django_filters
from django import forms
from django.forms import TextInput, NumberInput, Textarea

from home.models import FlightLog, Aircraft, Operator, Contact


class UserForm(UserCreationForm):

	class Meta:
		model = Operator
		fields = ['first_name', 'last_name', 'caa_code', 'email', 'username', 'file1', 'file2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['first_name'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Prenume'})
		self.fields['last_name'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Nume'})
		self.fields['caa_code'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Codul CAA fără ultimele 3 cifre'})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Adresa de e-mail'})
		self.fields['password1'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Introdu parola'})
		self.fields['password2'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Introdu parola din nou'})
		self.fields['file1'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Introdu certificatul A1/A3 -optional-'})
		self.fields['file2'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Introdu certificatul A2 -optional-'})


class AuthenticationNewForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter username'})
		self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter password'})


class ChangePasswordForm(PasswordChangeForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['old_password'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter your old password'})
		self.fields['new_password1'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter your new password'})
		self.fields['new_password2'].widget.attrs.update(
			{'class': 'form-control', 'placeholder': 'Please enter your new password again'})


# class FlightFilters(django_filters.FilterSet):
# 	list_of_flights = [(flights.longitude, flights.latitude) for flights in FlightLog.objects.filter(active=True)]
#
# 	longitude = django_filters.ChoiceFilter(choices=list(set(list_of_flights)))
#     latitude = django_filters.CharFilter(lookup_expr='icontains', label='Latitude')
#     batteries_flown = django_filters.CharFilter(lookup_expr='icontains', label='Number of batteries')
#
#
# 	class Meta:
# 		model = FlightLog
# 		fields = ['longitude', 'latitude', 'batteries_flown']
#
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
#
# 		self.filters['longitude'].field.widget.attrs.update(
#             {'class': 'form-control', 'placeholder': 'Please enter longitude'})
# 		self.filters['latitude'].field.widget.attrs.update(
#             {'class': 'form-control', 'placeholder': 'Please enter latitude'})
# 		self.filters['batteries_flown'].field.widget.attrs.update({'class': 'form-select'})


class FlightUpdateForm(forms.ModelForm):
	class Meta:
		model = FlightLog
		fields = '__all__'
		widgets = {
			'aircraft': forms.Select(attrs={'placeholder': 'Selectează drona', 'class': 'form-select'}),
			'latitude': NumberInput(attrs={'placeholder': 'Latitudinea', 'class': 'form-control'}),
			'longitude': NumberInput(attrs={'placeholder': 'Longitudinea', 'class': 'form-control'}),
			'details': Textarea(attrs={'placeholder': 'Detalii de zbor', 'class': 'form-control', 'rows': 3}),
			'batteries_flown': NumberInput(attrs={'placeholder': 'Numărul bateriilor zburate', 'class': 'form-control'}),
		}


class FlightCreateForm(forms.ModelForm):
	class Meta:
		model = FlightLog
		fields = [
			'aircraft', 'latitude', 'longitude', 'details', 'batteries_flown'
		]
		widgets = {
			'aircraft': forms.Select(attrs={'placeholder': 'Selectează drona', 'class': 'form-select'}),
			'latitude': NumberInput(attrs={'placeholder': 'Latitudinea', 'class': 'form-control'}),
			'longitude': NumberInput(attrs={'placeholder': 'Longitudinea', 'class': 'form-control'}),
			'details': Textarea(attrs={'placeholder': 'Detalii de zbor', 'class': 'form-control'}),
			'batteries_flown': NumberInput(attrs={'placeholder': 'Numărul bateriilor zburate', 'class': 'form-control'}),

		}


class AircraftCreateForm(forms.ModelForm):
	class Meta:
		model = Aircraft
		fields = ['name']
		widgets = {
			'name': TextInput(attrs={'placeholder': 'Numele dronei', 'class': 'form-control'})
		}


class ContactCreateForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'last_name': TextInput(attrs={'placeholder': 'Nume', 'class': 'form-control'}),
			'first_name': TextInput(attrs={'placeholder': 'Prenume', 'class': 'form-control'}),
			'question': Textarea(attrs={'placeholder': 'Spune-ne ce te interesează', 'class': 'form-control'}),
			'email': TextInput(attrs={'placeholder': 'Adresa e-mail', 'class': 'form-control'}),
		}


# class PDFUploadCreateForm(forms.ModelForm):
# 	class Meta:
# 		model = PDFUpload
# 		fields = '__all__'
# 		widgets = {
# 			'name': TextInput(attrs={'placeholder': 'Certificatul A1/A3 sau A2?', 'class': 'form-control'}),
# 		}

class OperatorUpdateForm(forms.ModelForm):
	class Meta:
		model = Operator
		fields = ['email', 'file1', 'file2']
		widgets = {
			'email': TextInput(attrs={'placeholder': 'Update e-mail', 'class': 'form-control'}),
		}


class PassResetForm(PasswordResetForm):
	class Meta:
		model = Operator
		fields = ['email']
		widgets = {
			'email': TextInput(attrs={'placeholder': 'Trimite e-mail de resetare a parolei', 'class': 'form-control'}),
		}
