from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def create_user(request):
    print("POST info submitted")
    #Form info sent to terminal as a dicitonary
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context={
        "name_on_template": name_from_form,
        "email_on_template": email_from_form,
    }
    request.session["name"] = name_from_form
    request.session['email'] = email_from_form
    print(name_from_form)
    print(email_from_form)
    return redirect("/success")

def success(request):
    return render(request, "success.html")

def logout(request):
    del request.session['name']
    return redirect('/')
