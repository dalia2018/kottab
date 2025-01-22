from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth.models import Group


# Create your views here.
def test(request):
    return render(request,'login.html')


def add_user(request):
    if request.method == "POST":
        form=add_user_form(request.POST)
                
        if form.is_valid():
            selected_group=request.POST.get('groups')
            new_user=form.save()
            group=Group.objects.get(pk=selected_group)
            group.user_set.add(new_user)
            
            return redirect('manage_users')  
    else:
        form=add_user_form()
    
    return render(request,'add_user.html',{'form':form})

def edit_profile(request):
    user_data=get_object_or_404(User,pk=request.user.pk)
    form = user_form(instance=user_data)
    if request.method == 'POST':
        form = user_form(request.POST,instance=user_data)
        if form.is_valid():
            form.save()    
            return redirect('welcome')
    
    return render(request,'profile.html',{'form':form,'user_data':user_data})