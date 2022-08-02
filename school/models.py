from django.db import models

standard_choices=(
    ('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
    ('4th','4th'),
    ('5th','5th'),
    ('6th','6th'),
    ('7th','7th'),
    ('8th','8th'),
    ('9th','9th'),
    ('10th','10th'),
)

section_choices=(
    ('section-A','section-A'),
    ('section-B','section-B'),
    ('section-C','section-C'),
)
# Create your models here.
#creating the register student model by using the models fields
class registerstudent(models.Model):
    #declaring the model fields with the the model field types
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)

    #declaring the standard field with choices of standard_choices
    standard=models.CharField(choices=standard_choices,max_length=25)

    #declaring the section field with choices of standard_choices
    section=models.CharField(choices=section_choices,max_length=25)
    stream=models.CharField(max_length=25)
    rollno=models.CharField(max_length=25)

    #declaring the profile pic as filefield and uploading the photos to images folder
    profile_pic=models.FileField(upload_to='images/')
    dob=models.DateField(max_length=25)

    #saving the object as first name
    def __str__(self):
        return self.first_name


#creating the register teacher model by using the models fields
class registerteacher(models.Model):

    #declaring the model fields with the the model field types
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    classes=models.CharField(max_length=25)
    id=models.CharField(max_length=25,primary_key=True)
    subject=models.CharField(max_length=25)

    #declaring the profile pic as filefield and uploading the photos to images folder
    profile_pic = models.FileField(upload_to='images/')
    dob=models.DateField(max_length=25)

    #saving the contact no as the integer field
    contact_no=models.IntegerField()
    def __str__(self):
        return self.first_name