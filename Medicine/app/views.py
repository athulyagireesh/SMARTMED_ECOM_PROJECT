# from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Medicine
from django.contrib.auth.decorators import login_required



def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        User.objects.create_user(username=name, password=password)

        return redirect('login')

    return render(request, 'register.html')





def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('employee_dashboard')

        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# @login_required
# def employee_dashboard(request):
#     employee = Medicine.objects.get(user=request.user)
#     tasks = Task.objects.filter(assigned_to=employee)
#     return render(request, 'employee_dashboard.html', {'tasks': tasks})


# @login_required
# def add_employee(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         phone = request.POST['phone']
#         department = request.POST['department']
#         designation = request.POST['designation']

#         user = User.objects.create_user(username=username, email=email, password=password)
#         Medicine.objects.create(user=user, phone=phone, department=department, designation=designation)

#         return redirect('employee_list')

#     return render(request, 'add_employee.html')


# @login_required
# def employee_list(request):
#     employees =  Medicine.objects.all()
#     return render(request, 'employee_list.html', {'employees': employees})


# @login_required
# def assign_task(request):
#     employees =  Medicine.objects.all()

#     if request.method == "POST":
#         title = request.POST['title']
#         description = request.POST['description']
#         deadline = request.POST['deadline']
#         employee_id = request.POST['employee']

#         employee =  Medicine.objects.get(id=employee_id)

#         Task.objects.create(
#             title=title,
#             description=description,
#             deadline=deadline,
#             assigned_to=employee
#         )

#         return redirect('admin_dashboard')

#     return render(request, 'assign_task.html', {'employees': employees})


# @login_required
# def update_status(request, id):
#     task = get_object_or_404(Task, id=id)

#     if request.method == "POST":
#         task.status = request.POST['status']
#         task.save()
#         return redirect('employee_dashboard')

#     return render(request, 'update_status.html', {'task': task})