from django.shortcuts import render
from formapp.Feedback import Feedbackform
from django.core import validators
def View_feedback(request):
    submit=False
    name=""
    email=""
    phone=""
    sub=""
    f=Feedbackform()
    if(request.method=='POST'):
        f=Feedbackform(request.POST)
        if(f.is_valid()):
            name=f.cleaned_data['name']
            email=f.cleaned_data['email']
            phone=f.cleaned_data['phone']
            sub=f.cleaned_data['sub']
            submit=True
            return render(request,'Pages/index.html',{"f":f,"submit":submit,"name":name,"email":email,"phone":phone,
            "sub":sub})
        else:
            pass
    else:
        f=Feedbackform()        
    return render(request,'Pages/index.html',{"f":f})


def fed_submited(request):
    return render(request,"Pages/submited.html")

