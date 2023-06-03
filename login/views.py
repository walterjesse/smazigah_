from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from login.forms import SignupForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('register')

            # Additional validation and error handling if needed

            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
        else:
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{field}: {error}")
            messages.error(request, "Failed to create an account. Please correct the following errors:")
            messages.error(request, error_messages)
            return redirect('register')
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form})


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')
        except Exception as e:
            messages.error(request, "Failed to log in. Please try again later.")
            print(f"Login Error: {str(e)}")

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from .forms import ContactForm


@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sender_email = form.cleaned_data['email']
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                sender_email,
                ['smazigah@gmail.com'],
                fail_silently=False,
            )
            return redirect('success')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
