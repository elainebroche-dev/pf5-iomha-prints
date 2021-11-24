from django.forms.widgets import ClearableFileInput, SelectDateWidget
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'custom_widget_templates/custom_clearable_file_input.html'

class CustomSelectDateWidget(SelectDateWidget):
    template_name = 'django/forms/widgets/select_date.html'
    