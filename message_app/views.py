from django.shortcuts import render,HttpResponse,redirect
from .models import Msg

# Create your views here.

def home(request):
    return HttpResponse("This is Home page")

def create(request):
    #print("Request is:", request.method)
    if request.method=='POST':
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        # print("Name:",n)
        # print("Email:",mail)
        # print("Mobile:",mob)
        # print("Message:",msg)

        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()

        # return HttpResponse("Fetched values")
        return redirect('/output')
    else:
        return render(request,'create.html')

def output(request):
    m=Msg.objects.all()
    # print(m)
    context={}
    context['data']=m
    
    return render(request,'dashboard.html',context)

def delete(request,rid):
    #print("Id to be deleted:",rid)
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/output') 
    #return HttpResponse("Id to be deleted:"+rid)

def edit(request,rid):
    #print("Id to be edited:",rid)
    if request.method=="POST":
        un=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['mobile']
        umsg=request.POST['msg']

        m=Msg.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umob,msg=umsg)

        return redirect('/output')
    else:
        m=Msg.objects.get(id=rid)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    
    
    return HttpResponse("Id to be edited:"+ rid)