from django.contrib import admin
from . import models

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'createdAt')
    search_fields = ('fullName', 'content')

    def has_add_permission(self, request):
        # No one can add bookings via admin
        return False

    def has_change_permission(self, request, obj=None):
        # Superuser can view all, assigned staff can edit only status if needed
        if request.user.is_superuser:
            return True
        if obj and obj.assigned_to and obj.assigned_to.user == request.user:
            return True  # can view/edit only assigned bookings
        return False

    def has_delete_permission(self, request, obj=None):
        return False  


class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'position')
    search_fields = ('fullName', 'position')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'created_at')
    search_fields = ('firstName', 'lastName', 'email')
    list_filter = ('created_at',)

    def has_add_permission(self, request):
        # No one can add bookings via admin
        return False

    def has_change_permission(self, request, obj=None):
        # Superuser can view all, assigned staff can edit only status if needed
        if request.user.is_superuser:
            return True
        if obj and obj.assigned_to and obj.assigned_to.user == request.user:
            return True  # can view/edit only assigned bookings
        return False

    def has_delete_permission(self, request, obj=None):
        return False  


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    search_fields = ('title','summary', 'excerpt', 'author')
    list_filter = ('date_posted', 'author',)
    autocomplete_fields = ('author',)
    prepopulated_fields = {}
    exclude = ('slug',)  

admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Testimonial, TestimonialAdmin)
admin.site.register(models.staffMember, StaffMemberAdmin)
admin.site.register(models.Booking, BookingAdmin)
admin.site.register(models.BlogPost, BlogPostAdmin)
