from django.forms import ModelForm
from store.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'number', 'email', 'comment']
