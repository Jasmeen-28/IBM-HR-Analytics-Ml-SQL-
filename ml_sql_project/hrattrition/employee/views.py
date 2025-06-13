from .form import EmployeeForm
from .prediction import predict_employee
from .models import Employee
from django.shortcuts import render

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            data_dict = form.cleaned_data
            prediction = predict_employee(data_dict)
            employee.Attrition = prediction
            employee.save()  
            print('employee data', employee)
            return render(request, 'employees/result.html', {'attrition': prediction, 'employee': employee})
        else:
            print("Form errors:", form.errors)
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})


