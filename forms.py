from django import forms
from .models import Ticket, TicketComment, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TicketCreateForm(forms.ModelForm):
    # Using a simple FileField without widget customization for multiple files
    # The multiple file handling will be done in the view
    attachments = forms.FileField(required=False)
    
    class Meta:
        model = Ticket
        fields = ['subject', 'description', 'category', 'priority']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class TicketUpdateForm(forms.ModelForm):
    attachments = forms.FileField(required=False)
    
    class Meta:
        model = Ticket
        fields = ['subject', 'description', 'category', 'status', 'priority', 'assigned_to']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = TicketComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
        labels = {
            'content': '',
        }

class TicketFilterForm(forms.Form):
    SORT_CHOICES = (
        ('created_at', 'Date Created'),
        ('updated_at', 'Last Updated'),
        ('priority', 'Priority'),
        ('status', 'Status'),
        ('comments_count', 'Most Comments'),
        ('upvotes', 'Most Upvotes'),
    )
    
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search tickets...'}))
    status = forms.ChoiceField(required=False, choices=[(None, '-- Status --')] + list(Ticket.STATUS_CHOICES))
    category = forms.ModelChoiceField(required=False, queryset=Category.objects.all(), empty_label='-- Category --')
    priority = forms.ChoiceField(required=False, choices=[(None, '-- Priority --')] + list(Ticket.PRIORITY_CHOICES))
    sort_by = forms.ChoiceField(required=False, choices=SORT_CHOICES, initial='updated_at')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})