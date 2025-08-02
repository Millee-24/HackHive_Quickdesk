from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'bio', 'profile_picture',
            'notify_ticket_created', 'notify_ticket_updated', 'notify_ticket_status_changed', 'notify_ticket_comment'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a fieldset for notification settings
        for field_name in ['notify_ticket_created', 'notify_ticket_updated', 'notify_ticket_status_changed', 'notify_ticket_comment']:
            self.fields[field_name].widget.attrs.update({'class': 'form-check-input'})