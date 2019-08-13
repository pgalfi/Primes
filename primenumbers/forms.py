from django import forms
from django.forms import Form


class GetPrimeNumbersParamsForm(Form):
    n = forms.IntegerField(min_value=1)
    page = forms.IntegerField(min_value=1, required=False, initial=1)
    page_size = forms.IntegerField(min_value=1, required=False, initial=None)
    start = forms.IntegerField(min_value=1, required=False, initial=1)

    def clean_page(self):
        if not self.cleaned_data['page']:
            return 1
        return self.cleaned_data['page']

    def clean_start(self):
        if not self.cleaned_data['start']:
            return 1
        return self.cleaned_data['start']

