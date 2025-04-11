# employee/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# Create (Insert)
def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        Employee.objects.create(name=name, email=email, department=department, salary=salary)
        return redirect('list_employees')

    return render(request, 'employee/add_employee.html')


# Read (View All)
def list_employees(request):
    employees = Employee.objects.all()
    return render(request, "employee/list_employees.html", {"employees": employees})

# Update
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.department = request.POST.get("department")
        employee.salary = request.POST.get("salary")
        employee.save()
        return redirect("list_employees")

    return render(request, "employee/update_employee.html", {"employee": employee})


# Delete
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect("list_employees")
    return render(request, "employee/delete_employee.html", {"employee": employee})

