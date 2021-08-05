from django import forms

class sql_form(forms.Form):
    sql_syntax=forms.CharField(label="sql_syntax")