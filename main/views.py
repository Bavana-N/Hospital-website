from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import *
# Register View
def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        print("Username:", username)

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        print(User.objects.filter(username=username).exists())

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists,Please login.')
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'register.html')
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')

def Home(request):
    dept = Department.objects.all()
    doc = Doctor.objects.all()
    return render(request, 'bootstrap.html',{'department':dept,'doctor':doc})
def Cardiology(request,id):
    serv = Department.objects.get(id=id)
    #serv = Department.objects.all()
    return render(request, 'cardiology.html',{'service':serv})
def BookAppointment(request, id):
    doctor = Doctor.objects.get(id=id)
    # return render(request, 'doc1.html', {'doctor': doctor})
 
    print("Book view called")
    if request.method == "POST":

        Appointment.objects.create(
            user=request.user,
            doctor=doctor,
            appointment_date=request.POST.get("date"),
            time_slot=request.POST.get("time_slot"),
            visit_type=request.POST.get("visit_type"),
            patient_name=request.POST.get("patient_name"),
            phone_number=request.POST.get("phone_number"),
            reason=request.POST.get("reason"),
        )

        messages.success(request, "✅ Appointment Booked Successfully!")
        return redirect('book_appo1', id=id)   # Redirect back to same page
    return render(request, 'doc1.html', {'doctor': doctor})
# def book_appo1(request):
    # return render(request, 'doc1.html')
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


