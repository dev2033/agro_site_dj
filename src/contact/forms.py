from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма контактов"""
    name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={"name": "name"}))
    email = forms.EmailField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"name": "email"})
    )
    phone = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"name": "phone"})
    )
    subject = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"name": "subject"})
    )
    message = forms.TextInput(attrs={"name": "message"})

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')

    def clean_email(self):
        email = self.cleaned_data['email']

        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Данный почтовый адрес, занят!'
            )
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if Contact.objects.filter(phone=phone).exists():
            raise forms.ValidationError(
                f'Данный номер телефона, уже занят!'
            )
        return phone
