from .models import Candidates
from django.forms import ModelForm,DateInput,IntegerField
class CandidatesForm(ModelForm):
    votes=IntegerField(initial=0,required=False)
    class Meta:
        model = Candidates
        fields='__all__'
        widgets={
            'dob':DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','placeholder':'Select a date','type':'date'})
        }