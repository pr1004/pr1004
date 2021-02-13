from django.views.generic import TemplateView
from .forms import SignInForm, LoginForm
from .models import User
from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages

def sign_up(request):
	form = SignInForm()
	context = {'form': form }
	if request.method == 'POST':
		if not User.objects.filter(email=request.POST['email']):
			password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
			password = password.decode('utf-8')
			User.objects.create(full_name=request.POST['full_name'], email=request.POST['email'], password=password)
			messages.success(request, '아이디생성완료')
			return redirect('/')
		else:
			messages.error(request, '존재하는 이메일입니다.')
			return render(request, 'sign_up.html', context)
	return render(request, 'sign_up.html', context)

def login(request):
	form = LoginForm()
	context = {'form': form }
	if request.method == 'POST':
		user = User.objects.filter(email=request.POST['email'])
		if user:
			if bcrypt.checkpw(request.POST['password'].encode('utf-8'), user[0].password.encode('utf-8')):
				messages.success(request, '로그인성공')
				request.session['user'] = user[0].id
				rd = redirect('/')
				rd.set_cookie('key', request.session.get('user'))
				return rd
			else:
				messages.error(request, '이메일 또는 패스워드가 잘못되었습니다.')
				return render(request, 'login.html', context)
		else:
			messages.error(request, '이메일 또는 패스워드가 잘못되었습니다.')
			return redirect('login')
	return render(request, 'login.html', context)

def logout(request):
	response = redirect('/')
	request.session.flush()
	response.delete_cookie('key')

	return response