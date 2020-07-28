from django.forms import ModelForm
from .models import loanModel

class LoanForm(ModelForm):
    class Meta:
        model = loanModel
        fields = ['Name', 'phone_number', 'identity_no', 'Address', 'reason']