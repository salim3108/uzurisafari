from django import forms
from . import models
from django_countries.widgets import CountrySelectWidget
from tinymce.widgets import TinyMCE


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = models.Testimonial
        fields = ['fullName', 'content', 'displayPicture']
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'displayPicture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'fullName': 'Full Name',
            'content': 'Testimonial Content',
            'displayPicture': 'Display Picture',
        }
        help_texts = {
            'fullName': 'Enter your full name.',
            'content': 'Share your experience with us.',
            'displayPicture': 'Upload a picture to accompany your testimonial.',
        }
        error_messages = {
            'fullName': {
                'required': 'Please enter your full name.',
            },
            'content': {
                'required': 'Please provide your testimonial content.',
            },
            'displayPicture': {
                'invalid': 'The uploaded file is not a valid image.',
            },
        }

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = models.staffMember
        fields = ['fullName', 'position', 'profilePicture']
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'biography': forms.Textarea(attrs={'class': 'form-control'}),
            'profilePicture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'fullName': 'Full Name',
            'position': 'Position',
            'profilePicture': 'Profile Picture',
            'biography': 'Biography',
        }
        help_texts = {
            'fullName': 'Enter the full name of the team member.',
            'position': 'Enter the position of the team member.',
            'profilePicture': 'Upload a profile picture for the team member.',
            'biography': 'Write a brief biography for the team member.',
        }
        error_messages = {
            'fullName': {
                'required': 'Please enter the full name of the team member.',
            },
            'position': {
                'required': 'Please enter the position of the team member.',
            },
            'biography': {
                'required': 'Please provide a biography for the team member.',
            },
            'profilePicture': {
                'invalid': 'The uploaded file is not a valid image.',
            },
        }


class ContactForm(forms.Form):
    fullName = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")
    

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost

        excerpt = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'summary': forms.TextInput(attrs={'class': 'form-control', 'cols': 40, 'rows': 10}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Blog Post Title',
            'image': 'Featured Image',
            'summary': 'Summary',
            'excerpt': 'Content',
            'author': 'Author Name',
        }
        help_texts = {
            'title': 'Enter the title of the blog post.',
            'image': 'Upload a featured image for the blog post.',
            'sumary': 'Enter a brief summary of the blog post.',
            'excerpt': 'Write the content of the blog post.',
            'author': 'Enter the name of the author.',
        }
        error_messages = {
            'title': {
                'required': 'Please enter a title for the blog post.',
            },
            'summary': {
                'required': 'Please provide a summary for the blog post.',
            },
            'excerpt': {
                'required': 'Please provide content for the blog post.',
            },
            'image': {
                'invalid': 'The uploaded file is not a valid image.',
            },
        }


class BookingForm(forms.ModelForm):
    # Extra field for country code (not stored directly in DB)
    country_code = forms.CharField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'country_code'})
    )

    phoneNumber = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '755...'})
    )

    class Meta:
        model = models.Booking
        fields = [
            'firstName', 'lastName', 'email', 'phoneNumber', 'nationality', 'region',
            'city', 'postal', 'budget', 'days', 'adventure', 'destination',
            'accommodation_type', 'accommodation_level', 'departure_date',
            'arrival_date', 'adults', 'children', 'additional_info'
        ]

        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'First'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Last'}),
             
            'region': forms.TextInput(attrs={'placeholder': 'Your region'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'city': forms.TextInput(attrs={'placeholder': 'Your city'}),
            'postal': forms.TextInput(attrs={'placeholder': 'Postal code'}),
            'budget': forms.NumberInput(attrs={'placeholder': 'e.g. 1500'}),
            'days': forms.NumberInput(attrs={'placeholder': 'e.g. 7'}),
            'adventure': forms.Select(choices=[
                ('', 'Select Adventure'),
                ('Safari', 'Safari'),
                ('Hiking', 'Hiking'),
                ('Beach', 'Beach'),
                ('Cultural Tour', 'Cultural Tour'),
            ]),
            'destination': forms.Select(choices=[
                ('', 'Select Destination'),
                ('Serengeti', 'Serengeti'),
                ('Kilimanjaro', 'Kilimanjaro'),
                ('Zanzibar', 'Zanzibar'),
                ('Ngorongoro', 'Ngorongoro'),
            ]),
            'accommodation_type': forms.Select(choices=[
                ('', 'Select Accommodation Type'),
                ('Hotel', 'Hotel'),
                ('Lodge', 'Lodge'),
                ('Camp', 'Camp'),
            ]),
            'accommodation_level': forms.Select(choices=[
                ('', 'Select Accommodation Level'),
                ('Standard', 'Standard'),
                ('Luxury', 'Luxury'),
                ('Budget', 'Budget'),
            ]),
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'additional_info': forms.Textarea(attrs={'placeholder': 'Any extra details...', 'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get("country_code")
        number = cleaned_data.get("phoneNumber")

        if code and number:
            # Merge into single phone number
            cleaned_data["phoneNumber"] = f"{code}{number}"
        elif number:
            # fallback if no country code selected
            cleaned_data["phoneNumber"] = number

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Ensure final phoneNumber includes country code
        instance.phoneNumber = self.cleaned_data.get("phoneNumber")
        if commit:
            instance.save()
        return instance