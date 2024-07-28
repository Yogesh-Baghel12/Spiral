from django.shortcuts import render,redirect
from CRUD.models import Employee

# Create your views here.


def INDEX(request):
    emp=Employee.objects.all()
    context={
        "emp":emp,
    }
    
    return render(request,'indexs.html',context)

def ADD(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        designation=request.POST.get('designation')
        department=request.POST.get('department')
        manager=request.POST.get('manager')
        active=request.POST.get('status')
        
        emp=Employee(
            name=name,
            email=email,
            mobile=mobile,
            address=address,
            designation=designation,
            department=department,
            manager=manager,
            active=active,
        )
        emp.save()
        return redirect('home')
            
        
        
    return render(request,'indexs.html',)
    
    


def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        designation=request.POST.get('designation')
        department=request.POST.get('department')
        manager=request.POST.get('manager')
        status=request.POST.get('status')
        
        
        emp=Employee(
            id=id,
            name=name,
            email=email,
            mobile=mobile,
            address=address,
            designation=designation,
            department=department,
            manager=manager,
            active=status,
        )
        emp.save()
    return redirect('home')

def delete(request,id):
    emp=Employee.objects.filter(id=id).delete()
    context={
        'emp':emp,
    }
    return redirect('home')
        