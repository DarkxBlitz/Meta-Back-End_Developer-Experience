from django import forms


FOOD_SERVICE = (
    ("1", "Delivery"),
    ("2", "Order In"),
    ("3", "Take out"),
)

#TIP: After max_length=200 you can add another parameter called required = False which means that the user doesn't have to input that exact field if its not required
#Example: first_name = forms.CharField(max_length=200, required = False)
#create your form
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    food_service = forms.ChoiceField(choices = FOOD_SERVICE)
    time_log = forms.TimeField()
    