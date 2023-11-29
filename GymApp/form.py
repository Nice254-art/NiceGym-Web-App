from django import forms
from GymApp.models import Member, Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields =['firstname','lastname','email','age','phone','classes']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields =['firstname', 'lastname', 'email', 'password']