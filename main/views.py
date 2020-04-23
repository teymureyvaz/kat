from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View
from main.models import Profile
# Create your views here.


class IndexView(View):
	def get(self, request):
		return render(request,'index.html')

	def post(self,request):
		name = request.POST.get('name')
		mail = request.POST.get('mail')
		text = request.POST.get('text')
		profile = Profile()
		profile.name = name
		profile.mail = mail
		profile.text = text
		print(profile)
		#profile.save()
		return render(request,'index.html')


class ResultsView(View):
	def get(self, request):
		profiles = Profile.objects.all()
		#print(profiles)
		return render(request,'results.html',{"profiles":profiles})