from django.contrib import admin
from course.models import Course, Category
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'credits', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at','category')
    search_fields = ('title', 'description')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)


