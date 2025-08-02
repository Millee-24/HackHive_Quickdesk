from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model for the QuickDesk application.
    Extends the built-in AbstractUser to allow for future customization.
    """
    # Add custom fields here as needed
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Notification settings
    notify_ticket_created = models.BooleanField(default=True, help_text="Receive notifications when a new ticket is created")
    notify_ticket_updated = models.BooleanField(default=True, help_text="Receive notifications when a ticket is updated")
    notify_ticket_status_changed = models.BooleanField(default=True, help_text="Receive notifications when a ticket status changes")
    notify_ticket_comment = models.BooleanField(default=True, help_text="Receive notifications when a comment is added to a ticket")
    
    def __str__(self):
        return self.username
