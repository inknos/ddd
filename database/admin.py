from django.contrib import admin

# Register your models here.
from .models import Contributor, Institution, Action, Contribution

admin.site.register(Contributor)
admin.site.register(Institution)
admin.site.register(Action)
admin.site.register(Contribution)
