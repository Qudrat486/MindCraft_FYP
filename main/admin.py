from django.contrib import admin
from .models import *
# Register your models here.

class WhatYouWillLearnTabularInline(admin.TabularInline):
    model = WhatYouWillLearn
    
class RequirementsTabularInline(admin.TabularInline):
    model = Requirements
    
class courseAdmin(admin.ModelAdmin):
    inlines = [WhatYouWillLearnTabularInline, RequirementsTabularInline]

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Course, courseAdmin)
admin.site.register(Level)
admin.site.register(WhatYouWillLearn)
admin.site.register(Requirements)