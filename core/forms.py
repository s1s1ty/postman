from django import forms

from .models import SendProduct


class SendProductForm(forms.ModelForm):
    item_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    item_details = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    delivery_address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    payable_amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    delivery_charge = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = SendProduct
        exclude = ('qr_code', 'user')
        fields = '__all__'


class SendProductForm2(forms.ModelForm):
    pass
