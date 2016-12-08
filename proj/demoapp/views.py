from django.shortcuts import render
from .tasks import async_write
# Create your views here.

def demo(request):
	template = 'demoapp/demo.html'
	context = {}
	context['test'] = 'test'
	if request.method == 'GET':
		data = request.GET
		print 'data', data
		print 'calling async_write'
		async_write.delay((int(data['ping_times'])))
	return render(request, template, context)
