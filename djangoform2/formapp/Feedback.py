from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
class Feedbackform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    phone=forms.CharField()
    #psrd=forms.CharField(validators=password)
    sub=forms.CharField(widget=forms.Textarea,validators=
    [validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    
    def password(self):
        psrd=self.cleaned_data['pass']
        rpsrd=self.cleaned_data['pass']
        if(psrd!=rpsrd):
            raise forms.ValidationError("password dont match")


    def clear(self):
        form_cleaned_data=super().clean()
        inputname=form_cleaned_data['name']
        if(len(inputname)<3):
            raise forms.ValidationError("User Name Must be 3 charate  or above")

        inputemail=form_cleaned_data['email']
        if(not inputemail.endswith('.com') and not inputemail.endswith('.net')):
            raise forms.ValidationError("enter valid email") 

        inputnum=form_cleaned_data['phone']
        if(not len(inputnum)==10):
            raise forms.ValidationError("number vant be less than 10")

        inputsub=self.cleaned_data['sub']
        if(not len(inputsub)==20 ):
            raise forms.ValidationError("must have to write minimum 50 char")

        return form_cleaned_dat    

        
