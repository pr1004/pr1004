from django.views.generic import TemplateView
from .forms import LoginForm
from .models import User
from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages

def index(request):
	if request.method == 'POST':
		if not User.objects.filter(email=request.POST['email']):
			password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt()) 
			User.objects.create(full_name=request.POST['full_name'], email=request.POST['email'], password=password)
			messages.success(request, '아이디생성완료')
			return redirect('/')
		else:
			messages.error(request, '존재하는 이메일입니다.')
			redirect('index')
	form = LoginForm()
	context = {'form': form }
	return render(request, 'login.html', context)