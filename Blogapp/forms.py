from django import forms
    


class ContactForm(forms.Form):
    name=forms.CharField(max_length=40,required=True,label="Name")
    email=forms.EmailField(required=True,label="Email")
    message=forms.CharField(required=True,label="Message")