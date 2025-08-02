from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Ticket, TicketComment

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'description', 'category', 'attachment']

class CommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ['comment']
