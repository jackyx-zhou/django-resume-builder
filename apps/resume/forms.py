from django import forms

from models import ResumeItem, Resume

class ResumeForm(forms.ModelForm):
    """
    A form for creating and editing resume. Note that 'user' is not
    included: it is always set to the requesting user.
    """
    class Meta:
        model = Resume
        fields = ['title']

class ResumeItemForm(forms.ModelForm):
    """
    A form for creating and editing resume items. Note that 'user' is not
    included: it is always set to the requesting user.
    """
    class Meta:
        model = ResumeItem
        fields = ['jobTitle', 'company', 'start_date', 'end_date', 'description']

class SelectResumeItemForm(forms.Form):
    item = forms.ModelChoiceField(queryset=ResumeItem.objects.all().order_by('-start_date'), empty_label="Select Resume Item", widget=forms.Select(attrs={'class':'form-control'}))
