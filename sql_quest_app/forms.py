from django import forms

# class sql_form(forms.Form):
#     sql_syntax=forms.CharField(label="sql_syntax")

class sql_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "
    sql_syntax = forms.CharField(label='',widget=forms.Textarea(attrs={'class': 'from-control mx-2 col-10', 'cols': '120', 'rows': '5','label':'SQL'}))
