from django.contrib import admin
from .models import *


admin.site.register(login)
admin.site.register(Profile)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'status')
    list_display_links = ('id','category')
    list_filter = ('date_created',)
    list_per_page = 10
    list_editable = ('status',)
admin.site.register(Categories, CategoriesAdmin)

class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_category', 'category', 'status')
    list_filter = ('category', 'date_created')
    list_editable = ('status',)
admin.site.register(sub_categories, SubCategoriesAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'sub_category', 'status')
    list_filter = ('date_created', 'sub_category', 'subject')
    list_editable = ('status',)
    list_per_page = 25
admin.site.register(Subjects, SubjectAdmin)

admin.site.register(Question)
admin.site.register(Center)