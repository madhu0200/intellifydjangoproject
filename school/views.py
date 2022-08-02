from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render


from .forms import *
# Create your views here.

#defining the home function
def home(request):

    #returning the home.html page as the request response
    return render(request,'home.html')

#defining the register2 function
# data variable is assigned with the value passed by the url
def register2(request,data):

    # returning the home3.html page as the request response and passing the dictionary with key as context and value as data
    return render(request,'home2.html',{'context':data})


#defining the register3 function
# data variable is assigned with the value passed by the url
def register3(request,data):

    if request.method=='POST':

        #checking the data value
        # if it is student or not
        if data=='student':

            # if data value is student passing the values to the registerstudentForm
            form=registerstudentForm(request.POST,request.FILES)
        else:

            # if data value is not student passing the values to the registerteacherForm
            form=registerteacherForm(request.POST,request.FILES)

       #validating the values with the form
        if form.is_valid():

            #if form is valid saving the form object
            form.save()

            #passing a confirmation message to the user it will shown in the home2.html
            messages.success(request,'registration successfully completed')

            #returning the home2.html as the request response
            return render(request,'home2.html',{'context':'signin'})
        else:

            #passing a confirmation message to the user it will shown in the home2.html
            messages.warning(request,'error occured!')

            #returning the home2.html as the request response
            return render(request,'home2.html',{'context':'register'})


#defining the register function
# data variable is assigned with the value passed by the url
def register(request,data):
    #checking the data variable if it is student or not
    if data=='student':

        #if the data is equal to student
        # returning the registerstudent.html as the request response
        return render(request,'registerstudent.html')
    else:


        #if the data is not equal to student
        # returning the registerteacher.html as the request response
        return render(request,'registerteacher.html')


#defining the signin function
# data variable is assigned with the value passed by the url
def signin(request,data):
    # returning the signin.html as the request response  and passing the dictionary with key as context and value as data
    return render(request,'signin.html',{'context':data})


#defining the signin2 function
# data variable is assigned with the value passed by the url
def signin2(request,data):
    if request.method=='POST':

        #checking the data variable
        if data=='teacher':

            #if it is teacher getting the values of id and dob passed by the form
            id=request.POST.get('id')
            dob = request.POST.get('dob')

            #getting objects from registerteacher table by filtering the id and dob and getting objects
            user=registerteacher.objects.filter(id=id,dob=dob).first()



            if user is not None:

                #if user object is not None
                # returning the teacher_profilepage.html as the request response  and passing the dictionary with key as context and value as user
                return render(request,'teacher_profilepage.html',{'context':user})
            else:
                # if there are no objects present in the table
                #showing error to the user
                messages.warning(request,'enter details correctly')
                # returning the signin.html as the request response  and passing the dictionary with key as context and value as data

                return render(request,'signin.html',{'context':data})
        else:

            #if it is teacher getting the values of id and dob passed by the form
            rollno=request.POST.get('rollno')
            dob = request.POST.get('dob')

            #getting objects from registerteacher table by filtering the id and dob and getting objects
            user=registerstudent.objects.filter(rollno=rollno,dob=dob).first()
            if user is not None:
                #if user object is not None
                # returning the student_profilepage.html as the request response  and passing the dictionary with key as context and value as user
                return render(request,'student_profilepage.html',{'context':user})
            else:
                # if there are no objects present in the table
                #showing error to the user
                messages.warning(request, 'enter details correctly')
                # returning the signin.html as the request response  and passing the dictionary with key as context and value as data
                return render(request,'signin.html',{'context':data})