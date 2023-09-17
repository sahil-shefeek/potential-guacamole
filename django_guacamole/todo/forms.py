from django import forms

class task_form(forms.Form):
    task = forms.CharField(label="Enter task")