# Register your models here.
from django.contrib import admin
from .models import Category
# admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
#    fields = ['name', 'parent_name', 'budget', 'date_of_budget']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Données du budget', {'fields': ['parent_name', 'date_of_budget', 'budget', 'type']}),
        ('Complément d\'info', {'fields': ['date_of_amount', 'amount', 'level'], 'classes': ['collapse']})
    ]
    list_display = ('name', 'parent_name', 'budget', 'date_of_budget', 'type')
    list_filter = ['parent_name', 'type', 'level']
    search_fields = ['name', 'parent_name', 'budget']

admin.site.register(Category, CategoryAdmin)