from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
	video_list = [
		{'id': '1', 'name': 'mov_bbb.mp4'},
		{'id': '2', 'name': 'mov_bbb.mp4'},
	]
	context = {
        'video_list': video_list,
    }
	return JsonResponse(video_list, safe=False)