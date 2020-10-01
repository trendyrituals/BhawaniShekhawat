from django.shortcuts import render
from .models import ProfileImg,Profile,Service,Training,DevServe,Consult
from .forms import ContactForm
# Create your views here.

def home(request):
	detail_one = Profile.objects.get(num='1')
	detail_two = Profile.objects.get(num='2')
	detail_three = Profile.objects.get(num='3')

	service_IT = Service.objects.get(name='IT Trainings & Seminars')
	service_Dev = Service.objects.get(name='Development')
	service_Consult = Service.objects.get(name='Full Time IT Consultant')

	profile_img = ProfileImg.objects.get(name='bhawani')

	context = {
		'one': detail_one,
		'two': detail_two,
		'three': detail_three,
		'IT': service_IT,
		'Dev': service_Dev,
		'Consult': service_Consult,
		'img': profile_img
	}
	return render(request,'index.html',context)

def development(request):
	page = Service.objects.get(name='Development')
	web = DevServe.objects.get(name='Web & App Development')
	soft = DevServe.objects.get(name='Software Development')
	robo = DevServe.objects.get(name='Robotics & AI Development')
	context = {
		'page':page,
		'web':web,
		'soft':soft,
		'robo':robo
	}
	return render(request,'development.html',context)

def training(request):
	training_two = Training.objects.get(year='Year 2018')
	training_one = Training.objects.get(year='Year 2019')
	service = Service.objects.get(name='IT Trainings & Seminars')
	context = {
		'one': training_one,
		'two': training_two,
		'page': service
	}
	return render(request,'training.html',context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid:
		detail = form.save(commit=False)
		detail.save()
		
	context = {
		'form':form
	}
	return render(request,'contact.html',context)

def consult(request):
	page = Consult.objects.get(id=1)
	context = {
		'page':page
	}
	return render(request,'consult.html',context)
