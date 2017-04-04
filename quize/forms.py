from django import forms
from .models import User, Contest, Category

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('cat',)

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('name','date', 'result',)