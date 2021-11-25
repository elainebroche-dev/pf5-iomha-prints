import datetime
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from iomha_prints.widgets import CustomClearableFileInput
from iomha_prints.widgets import CustomSelectDateWidget
from .models import Artist


class ArtistForm(forms.ModelForm):
    """
    - include all Artist fields in the form
    - apply formatting to the form fields
    - configure summernote widget for use by the 'bio' field
    - configure date selector widget for the 'dob' field
    - 'dob' field has a range of current year -10 to 1920 for artist
      year of birth
    """
    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    bio = forms.CharField(widget=SummernoteInplaceWidget())
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    today = datetime.datetime.now()
    dob = forms.DateField(label='Date of Birth', required=False,
                          widget=CustomSelectDateWidget(empty_label=(
                              "Choose Year", "Choose Month", "Choose Day"),
                              years=range(today.year - 10, 1920, -1),),)
