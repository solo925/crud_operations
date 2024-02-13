from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Employee

class RegisterEmployee(forms.ModelForm):
    class Meta:
       model = Employee
       fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super(RegisterEmployee,self).__init__(*args,  **kwargs)
        self.fields['position'].empty_label = "select"