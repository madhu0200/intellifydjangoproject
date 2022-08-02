from django import forms

from .models import *

#creating the student form using the registerstudent model by metioning fields
class registerstudentForm(forms.ModelForm):
    class Meta:
        model=registerstudent
        fields=['first_name','last_name','standard','section','stream','rollno','profile_pic','dob',]

#creating the teacher form using the registerteacher model by metioning fields
class registerteacherForm(forms.ModelForm):
    class Meta:
        model=registerteacher
        fields=['first_name','last_name','classes','subject','profile_pic','dob','contact_no','id']