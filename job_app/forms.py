from django import forms 
from job_app.models import EmployeeModel,Job_seeker 

class CarModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

class jobsekeerFrom(forms.ModelForm):
    class Meta:
        model=Job_seeker
        exclude = ['user']
    def save(self, commit=True, user=None):
        job_seeker = super().save(commit=False)
        if user:
            job_seeker.user = user
        if commit:
            job_seeker.save()
        return job_seeker



  