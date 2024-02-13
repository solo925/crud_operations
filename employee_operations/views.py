from django.shortcuts import render,redirect
from .forms import RegisterEmployee
from .models import Employee
from django.shortcuts import get_object_or_404

# Create your views here.

def register(request):
    
    form = RegisterEmployee()
    if request.method =='POST':
        form = RegisterEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form = RegisterEmployee()
            
    return render(request,'employee_operetions/register.html',{'form':form})


def List(request):
    employee = Employee.objects.all()
    return render(request,'employee_operetions/list.html',{'employee':employee})

def Update(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        form = RegisterEmployee(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RegisterEmployee(instance=employee)

    return render(request, 'employee_operetions/list.html', {'employee': [employee], 'form': form})

def Delete(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('list')
    


    
            


            
   
        
        
   
    

   