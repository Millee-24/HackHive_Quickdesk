import os
import sys
import django

# Add the project directory to the Python path
# This is crucial for Python to find your 'Quickdesk' module.
sys.path.append(r'E:\QUICKDESK')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QUICKDESK.settings')

# Initialize Django
django.setup()

# You can now import and use your Django models and other components
# For example, to print all users:
from django.contrib.auth import get_user_model
User = get_user_model()
print("All users:", User.objects.all())

# ... or any other Django-related logic you want to execute