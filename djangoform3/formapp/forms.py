from django import forms

class stdform(forms.Form):
    name=forms.CharField(label="Name")
    email=forms.EmailField(label="Email")
    phone=forms.CharField(label="Phone")
    password=forms.CharField(label="Password")
    Again_password=forms.CharField(label="Re-pass")

    def clean(self):
        print("validating start")
        std_cleaned_data=super().clean()
        name=std_cleaned_data['name']
        phone=std_cleaned_data['phone']
        pasd=std_cleaned_data['password']
        rpasd=std_cleaned_data['Again_password']
        if(name==""):
            raise forms.ValidationError("user field cant be mpty")
        elif(len(name)<3):
            raise forms.ValidationError("user name cant be less than 2 char")
        else:
            w=name.split()
            for i in w:
                if(not i.isalpha()):
                     raise forms.ValidationError("user field cant be number must char")

        if(phone==""):
            raise forms.ValidationError("phone field cant be empty")
        else:

            if phone and not phone.isdigit():
                raise forms.ValidationError("Phone number must contain only digits.")
    
        if(pasd==""):
            raise forms.ValidationError("phone field cant be empty")
        else:
            if pasd and rpasd and pasd != rpasd:
                raise forms.ValidationError("Passwords don't match.")

        return std_cleaned_data     

    
   
                         

                




