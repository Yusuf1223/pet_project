from django.forms import ModelForm, Form
from store.models import Feedback, Watch


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'number', 'email', 'comment']


# class FilterForm(ModelForm):
#     class Meta:
#         model = Watch
#         fields = ['bracelet_color', 'bracelet_material', 'bracelet_size', 'watch_color',
#                   'watch_material', 'watch_size', 'glass_material', 'price']

