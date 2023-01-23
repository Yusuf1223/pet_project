from django import forms
from store.models import Feedback, Watch


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'number', 'email', 'comment']


# class FilterForm(forms.ModelForm):
#     class Meta:
#         model = Watch
#         fields = ['bracelet_color', 'bracelet_material', 'bracelet_size', 'watch_color',
#                   'watch_material', 'watch_size', 'glass_material', 'price']

# class CartForm(forms.Form):
#     count = forms.Select(choices=(num for num in range()))
