from django.contrib import admin
from .models import loanModel

# Register your models here.
class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(loanModel, LoanAdmin)