from django.shortcuts import render
from formapp.forms import stdform

def formshow(request):
    obj=stdform()
    name=""
    email=""
    phone=""
    pasd=""
    rpasd=""
    submit=False
    if(request.method=='POST'):
        obj=stdform(request.POST)
        if(obj.is_valid()):
            name=obj.cleaned_data['name']
            email=obj.cleaned_data['email']
            phone=obj.cleaned_data['phone']
            pasd=obj.cleaned_data['password']
            rpasd=obj.cleaned_data['Again_password']
            print(obj.cleaned_data['name'])

    return render(request,"Pages/index.html",{"obj":obj,"name":name,"email":email,"phone":phone,
    "pasd":pasd,"rpds":rpasd})

