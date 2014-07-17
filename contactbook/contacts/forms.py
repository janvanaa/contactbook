from django import forms
from .models import Person, Company

class PersonForm(forms.ModelForm):                
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'address', 'city', 'postcode', 'phone', 'email', 'website', 'works_for', 'function', 'bank', )

class CompanyForm(forms.ModelForm):                
    class Meta:
        model = Company
        fields = ('name', 'branche', 'address', 'city', 'postcode', 'phone', 'email', 'website', 'kvk', 'btw', 'bank', )
