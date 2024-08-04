from django.shortcuts import render,redirect
from CRUD.models import Employee
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def INDEX(request):
    if not request.user.is_staff:
        return redirect('home')
    emp=Employee.objects.all()
    context={
        "emp":emp,
    }
    
    return render(request,'crud/indexs.html',context)

@login_required
def ADD(request):
    if not request.user.is_staff:
        return redirect('home')
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
            
        
        
    return render(request,'crud/indexs.html',)
    
    

@login_required
def update(request,id):
    if not request.user.is_staff:
        return redirect('home')
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

@login_required
def delete(request,id):
    if not request.user.is_staff:
        return redirect('home')
    emp=Employee.objects.filter(id=id).delete()
    context={
        'emp':emp,
    }
    return redirect('home')

@login_required
def search(request):
    if not request.user.is_staff:
        return redirect('home')
    query = request.GET.get('query', '')
    if query:
        emp = Employee.objects.filter(Q(name__icontains=query) | Q(id__icontains=query))
    else:
        emp = Employee.objects.all()  
    return render(request, 'crud/indexs.html', {'emp': emp})
        