from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView


class SignUpView(CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    success_url = '/thank-you/'


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'
