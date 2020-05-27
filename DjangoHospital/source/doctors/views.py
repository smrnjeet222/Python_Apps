from django.shortcuts import render
from .models import Doctor
from .forms import DoctorForm

# Create your views here.
def doctorDetailView(request):
    obj = Doctor.objects.get(id='2')
    # context = {
    #     'fname' : obj.fname,
    #     'bio' : obj.bio,
    # }
    context = {
        "object" : obj,
    }
    return render(request, 'doctors/doctor_details.html', context)

def doctorCreateView(request):
    form = DoctorForm()
    if request.method=='POST':
        form = DoctorForm(request.POST or None)   
        if form.is_valid():
            form.save()
            form = DoctorForm()
    context = {
        'form' : form,
    }
    return render(request, 'doctors/doctor_create.html', context)
