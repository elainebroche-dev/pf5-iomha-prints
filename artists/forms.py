from django import forms
from .models import Artist
from iomha_prints.widgets import CustomClearableFileInput, CustomSelectDateWidget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
import datetime


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    bio = forms.CharField(widget=SummernoteInplaceWidget())
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    today = datetime.datetime.now()
    dob = forms.DateField(label='Date of Birth', required=False,
        widget=CustomSelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range( today.year - 10, 1920, -1 ),),
    )