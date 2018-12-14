from django import forms
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.conf import settings

class ContactForm(forms.Form):
    your_name = forms.CharField(label=_("name"), max_length=100)
    email = forms.EmailField(label=_('email'), max_length=100)
    message = forms.CharField(label=_('message'), widget=forms.Textarea)

    def send_email(self):
        subject = "%s - %s" % (_("Feedback"), self.cleaned_data['your_name'])
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        send_mail(
            subject,
            message,
            from_email,
            [settings.MAIL_CONTACT]
        )
