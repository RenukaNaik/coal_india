from django.db.models import fields
from django.forms import ModelForm
from .models import CoalForm

from django import forms


# class BasicPoshanForm(forms.ModelForm):
#     class Meta:
#         model = BasicPoshanModel
#         fields = '__all__'

# class UploadPictureForm(forms.ModelForm):
#     class Meta:
#         model = UploadPictureModel
#         # fields = ('picture','name','nutri_nm','area','village','district','state','pincode','lat','lng')
#         fields = '__all__'
# class UploadWellPictureForm(forms.ModelForm):
#     class Meta:
#         model = UploadWellPictureModel
#         fields = ('picture','name','well_nm','radius','depth','level','village','district','state','pincode', 'lat', 'lng')

class Coalform(forms.ModelForm):
    class Meta:

       model=CoalForm
       fields='__all__'
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


        
# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None      
    
#     class Meta:
#         model=User
#         fields = ('username', 'email', 'password1', 'password2')
#         def save(self, commit=True):
#             user = super(NewUserForm, self).save(commit=False)
#             user.email = self.cleaned_data['email']
#             if commit:
#                 user.save()
#             return user