from django.shortcuts import render

def service(request):
	context = {'service':'active'}
	return render(request,'serv/services.html',context)
