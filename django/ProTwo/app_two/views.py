from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User
from app_two.forms import NewUserForm

def index(request):
    return render(request, "app_two/index.html")
    
def users(request):
    users_list = User.objects.all()
    my_dict = {"users": users_list}
    return render(request, "app_two/users.html", context=my_dict)
    
    
def user_sign_up(request):
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
            
        else:
            print("ERROR FORM INVALID")
        
    return render(request, "app_two/user_sign_up.html", {"form": form})
    
    
    
