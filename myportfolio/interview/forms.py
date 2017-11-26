from django import forms
from django.forms.widgets import RadioSelect
from .models import Question

class QuestionForm(forms.ModelForm):
    BOOL_CHOICES = ((True, 'job'), (False, 'nationality'))
    option = forms.ChoiceField(choices=BOOL_CHOICES, widget=RadioSelect)
    class Meta:
        model = Question
        fields = ('question','answer',)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs['placeholder'] = 'Add question here'
        self.fields['answer'].widget.attrs['placeholder'] = 'Add answer here'
