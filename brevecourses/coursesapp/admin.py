from django.contrib import admin
from .models import Comment, Course, Instructor, Price

class InstructorInline(admin.StackedInline):
    model = Instructor.courses.through

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    '''Admin View for Instructor'''
    filter_horizontal = ("courses",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''Admin View for Course'''
    inlines = [InstructorInline]

# Register your models here.
admin.site.register(Comment)
admin.site.register(Price)