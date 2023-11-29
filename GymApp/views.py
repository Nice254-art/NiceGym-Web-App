from django.shortcuts import render, redirect
from GymApp.models import Member, Booking
from GymApp.form import BookingForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        email=request.POST['email'], password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(email=request.POST['email'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(email=request.POST['email'],
                                        password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def classes(request):
    return render(request, 'classes.html')


def services(request):
    return render(request, 'services.html')


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            booking = form.save(commit=False)
            booking.save()

            # Redirect to a success page or do other actions
            return render(request, 'success.html', {'message': 'Booking successful!'})
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})


def gallery(request):
    return render(request, 'portfolio-details.html')


def success(request):
    return render(request, 'success.html')
