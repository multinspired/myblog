from django import forms

class FormName(forms.Form):
	name = forms.CharField(max_length=200,widget=forms.TextInput(
		attrs={'class':'w3-input w3-border', 'placeholder':'Name(s)', 'name':'name'}))
	