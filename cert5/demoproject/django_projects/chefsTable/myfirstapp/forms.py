from django import forms

from .models import InputForm

class LogForm(forms.ModelForm):
    class Meta:
        model = InputForm
        fields = '__all__' #--> the __all__ will import all the fields in the model, don't forget to update admin.py



'''
FOOD_SERVICE = (
    ("1", "Delivery"),
    ("2", "Order In"),
    ("3", "Take out"),
)
'''
#TIP: After max_length=200 you can add another parameter called required = False which means that the user doesn't have to input that exact field if its not required
#Example: first_name = forms.CharField(max_length=200, required = False)
#create your form

    