from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from User.views import user 

def send_confirmation_email(email, token):
    subject = 'Confirm Your Registration'
    html_message = render_to_string('registration/confirmation_email.html', {'token': token})
    plain_message = strip_tags(html_message)
    from_email = 'tawongachauluntha@gmail.com'
    to = user.email

    email_message = EmailMessage(subject, plain_message, from_email, [to])
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()
