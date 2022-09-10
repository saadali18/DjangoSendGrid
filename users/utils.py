from django.core.mail import EmailMessage


def send_email(to, reply_to, template_id, data):
    msg = EmailMessage(
        to=to,
        from_email="your sender email",
        reply_to=reply_to,
    )
    msg.template_id = template_id
    msg.dynamic_template_data = data
    msg.send()