from django import forms
from iomha_prints.widgets import CustomClearableFileInput
from .models import Print, PrintOption

class PrintForm(forms.ModelForm):

    class Meta:
        model = Print
        fields = '__all__'
        exclude = ('likes',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class PrintOptionForm(forms.ModelForm):

    class Meta:
        model = PrintOption
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'