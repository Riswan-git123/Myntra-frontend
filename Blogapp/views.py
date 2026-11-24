from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
# from django.core.paginator import Paginator




def Home(request):
    blog_title="Latest Posts"
    posts=[{"title":"Post1","content":"content of post 1"},
           {"title":"Post2","content":"content of post 2"},
           {"title":"Post3","content":"content of post 3"},
           {"title":"Post4","content":"content of post 4"},
           {"title":"Post5","content":"content of post 5"},
           {"title":"Post6","content":"content of post 6"},
           {"title":"Post7","content":"content of post 7"},
           {"title":"Post8","content":"content of post 8"}]

    # paginator=Paginator(posts,3)
    # page_number=request.GET.get('page')
    # page_obj=paginator.get_page(page_number)

    # print(paginator)
    

    
    
    return render(request,'index.html',{"title":blog_title,"posts":posts})



def Contact(request):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)

        names=request.POST['name']
        emails=request.POST['email']
        messages=request.POST['message']

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print("runs succesfully values are:")
            print(name)
            print(email)
            print(message)
           

        else:
            print("Invalid Contact Details")
            return render(request,'contact.html',{"name":names,"email":emails,"message":messages})
        
    return render(request,'contact.html')



def About(request):
    return render(request,'about.html')