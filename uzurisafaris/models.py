from django.db import models
from django.utils.text import slugify
import uuid
import random
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from utils.phone_codes import country_phone_codes


# Create your models here.

class Testimonial(models.Model):
    fullName = models.CharField(max_length=100)
    content = models.TextField()
    displayPicture = models.ImageField(upload_to='testimonials/')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullName
    


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class staffMember(models.Model):
    fullName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    profilePicture = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.fullName
    

class Booking(models.Model):
    # Personal info
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)  # Will store full number e.g. +255755123456
    nationality = CountryField()
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(max_length=20, blank=True, null=True)

    # Travel info
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    days = models.PositiveIntegerField(blank=True, null=True)
    adventure = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    accommodation_type = models.CharField(max_length=50, blank=True, null=True)
    accommodation_level = models.CharField(max_length=50, blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)

    # People
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)

    # Extra
    additional_info = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.destination}"
    

class BlogPost(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(staffMember, on_delete=models.CASCADE)
    summary = models.CharField(max_length=435, blank=True, null=True, )
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    excerpt = HTMLField()

    def save(self, *args, **kwargs):
        if not self.slug: 
            # Generate base slug
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            # Ensure uniqueness
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title