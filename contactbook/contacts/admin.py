from django.contrib import admin
from .models import Contact, Person, Company

class ContactPersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('naam', {'fields': ['first_name', 'last_name', ]}),
        ('lokatie', {'fields': ['address', 'postcode', 'city'], 'classes': ['collapse']}),
        ('contact', {'fields': ['phone', 'email', 'website'], 'classes': ['collapse']}),
        ('werk', {'fields': ['works_for', 'function', 'bank'], 'classes': ['collapse']}),
    ]
    
class ContactCompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('naam', {'fields': ['name', 'branche']}),
        ('lokatie', {'fields': ['address', 'postcode', 'city'], 'classes': ['collapse']}),
        ('contact', {'fields': ['phone', 'email', 'website'], 'classes': ['collapse']}),
        ('financieel', {'fields': ['kvk', 'btw', 'bank'], 'classes': ['collapse']}),        
    ]
    
admin.site.register(Person, ContactPersonAdmin)
admin.site.register(Company, ContactCompanyAdmin)