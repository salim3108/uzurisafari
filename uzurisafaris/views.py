from django.shortcuts import render, redirect
from django.contrib import messages
from . import models, forms
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
import csv
import uuid
import os
from django.utils.timezone import now

# Create your views here.
def homeView(request):
    testimonials = models.Testimonial.objects.all().order_by('-createdAt')
    return render(request, 'index.html', {'testimonials': testimonials})

def submit_testimonial(request):
    if request.method == 'POST':
        form = forms.TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Optional message
            messages.success(request, "Your testimonial has been submitted successfully!")
            # Redirect to confirmation page
            return redirect('confirmation')
    else:
        form = forms.TestimonialForm()
    return render(request, 'submit_testimonial.html', {'form': form})

def testimonial_confirmation(request):
    return render(request, 'confirmation.html')

def aboutView(request):
    members = models.staffMember.objects.all()
    return render(request, 'about.html', {'members': members})

def add_staff(request):
    if request.method == 'POST':
        form = forms.StaffMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Team member added successfully!")
            return redirect('add_member')
    else:
        form = forms.StaffMemberForm()
    return render(request, 'add_member.html', {'form': form})

def adventureView(request):
    return render(request, 'adventure.html')

def blogView(request):
    posts = models.BlogPost.objects.order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})

def blogPostView(request, slug):
    post = get_object_or_404(models.BlogPost, slug=slug)
    return render(request, 'blog_post.html', {'post': post})

def contactView(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if full_name and email and message:
            # === 1. Save to CSV ===
            csv_file = os.path.join(settings.BASE_DIR, "contact_messages.csv")
            file_exists = os.path.isfile(csv_file)

            with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Full Name", "Email", "Message", "Submitted At"])
                writer.writerow([full_name, email, message, now().strftime("%Y-%m-%d %H:%M:%S")])

            # === 2. Send Email Notification ===
            subject = f"New Contact Form Submission from {full_name}"
            body = f"""
You have received a new message:

Full Name: {full_name}
Email: {email}
Message: {message}

Submitted At: {now().strftime("%Y-%m-%d %H:%M:%S")}
"""
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "contact.html")
        
def beachView(request):
    return render(request, 'beach.html', {'adventure_type': 'beach'}) 

def hikingView(request):
    return render(request, 'hiking.html', {'adventure_type': 'hiking'})

def safariView(request):
    return render(request, 'safari.html', {'adventure_type': 'safari'})

def cityTourView(request):  
    return render(request, 'tour.html', {'adventure_type': 'cityTour'})

def bookingView(request):
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            # Merge country_code + phoneNumber
            country_code = form.cleaned_data.get("country_code")
            phone_number = form.cleaned_data.get("phoneNumber")
            booking.phoneNumber = f"{country_code}{phone_number}"

            booking.save()
            return redirect("success")  # You should have a success.html
    else:
        form = forms.BookingForm()

    return render(request, "booking.html", {"form": form})

def bookingSuccessView(request):
    """Simple success message after booking."""
    return render(request, "success.html")




