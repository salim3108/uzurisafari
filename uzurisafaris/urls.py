from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('testimonial/', views.submit_testimonial, name='testimonial'),
    path('testimonial/confirmation/', views.testimonial_confirmation, name='confirmation'),
    path('about/', views.aboutView, name='about'),
    path('about/add_staff/', views.add_staff, name='add_staff'),
    path('adventure/', views.adventureView, name='adventure'),
    path('blog/', views.blogView, name='blog'),
    path('blog/<slug:slug>/', views.blogPostView, name='blog_post'),
    path('contact/', views.contactView, name='contact'),
    path('adventure/beach/', views.beachView, name='beach'),
    path('adventure/hiking/', views.hikingView, name='hiking'),
    path('adventure/safari/', views.safariView, name='safari'),
    path('adventure/cityTour/', views.cityTourView, name='cityTour'),
    path('booking/', views.bookingView, name='booking'),
    path('booking/success/', views.bookingSuccessView, name='success'),
]
