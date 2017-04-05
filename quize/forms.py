from django import forms
from .models import User, Contest, Category

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('user',)
        


class CategoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['cat'].choices = (('sport','Спортивные'),('intel','Интеллектуальные'),('logic','Логические'))

	class Meta:
		model = Category
		fields = ('cat',)
		widgets = {'cat': forms.CheckboxSelectMultiple, }


class ContestForm(forms.ModelForm):
	class Meta:
		model = Contest
		fields = ('name','date', 'result',)
