from django import forms
from durationwidget.widgets import TimeDurationWidget

from .models import Client


class MyForm(forms.Form):
    name = forms.CharField(max_length=64, required=False, label="Введіть ім'я", disabled=True)
    email = forms.EmailField(initial="admin@admin.com", error_messages={
        'required': 'Please enter your available email'})
    password = forms.CharField(max_length=20, min_length=10,
                               required=False,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, initial="35",
                             help_text="Enter your current age")
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)
    # profile_picture = forms.ImageField(widget=forms.FileInput)
    # additional_file = forms.FileField(widget=forms.FileInput)    #
    birthday = forms.DateField(widget=forms.SelectDateWidget,
                               required=False)
    work_experience = forms.DurationField(required=False,
                                          widget=TimeDurationWidget(
                                              show_days=False))
    gender = forms.ChoiceField(required=False,
                               choices=[("1", "man"), ("2", "woman")])


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'second_email', 'name']
        # fields = '__all__'
