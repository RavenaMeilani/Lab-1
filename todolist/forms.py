from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label="Enter your task!", max_length=255)
    description = forms.CharField(label="Describe your task!", widget=forms.Textarea)