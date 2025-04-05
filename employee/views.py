# employee/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create (Insert)
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_employees")
    else:
        form = EmployeeForm()
    return render(request, "employee/add_employee.html", {"form": form})

# Read (View All)
def list_employees(request):
    employees = Employee.objects.all()
    return render(request, "employee/list_employees.html", {"employees": employees})

# Update
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("list_employees")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employee/update_employee.html", {"form": form})

# Delete
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect("list_employees")
    return render(request, "employee/delete_employee.html", {"employee": employee})

