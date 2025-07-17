from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_note'] 
        widgets = {
            'address':forms.Textarea(attrs={'row':3}),
            'order_notes': forms.Textarea(attrs={
                'row':5,
                'placeholder': 'if you have any notes please enter here otherwise leave it empty',
            }),
        }