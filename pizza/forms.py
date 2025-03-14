from django import forms
from .models import CollaborateRequest


class ContactUsForm(forms.ModelForm):
    """
    This class is used to create a form for the ContactUs model.
    **Context**
    ''fields''
        The fields of the form.
        `name` - The name of the person contacting
        `email` - The email of the person contacting
        `message` - The message of the person contacting
    """
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')