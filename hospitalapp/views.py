from django.shortcuts import render, redirect
from hospitalapp.models import Member, Response, Appointment, Users, ImageModel
from hospitalapp.forms import ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        response = Response(fullname=request.POST['fullname'], email=request.POST['email'],
                            subject=request.POST['subject'], message=request.POST['message'])
        response.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def index(request):
    if request.method == 'POST':
        appointment = Appointment(name=request.POST['name'],
                                  email=request.POST['email'],
                                  phone=request.POST['phone'],
                                  date=request.POST['date'],
                                  message=request.POST['message'])
        appointment.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def detail(request):
    detail = Appointment.objects.all()
    return render(request, 'detail.html', {'detail': detail})


def detail2(request):
    details2 = Users.objects.all()
    return render(request, 'detail2.html', {'detail2': details2})


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'adminhome.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
