from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
	# video_list = [
	# 	{'id': '1', 'url': 'test.mp4'},
	# 	{'id': '2', 'url': 'test2.mp4'},
	# ]
	r = requests.get('http://127.0.0.1:8000/videolist/')
	video_list = r.json()
	context = {
        'video_list': video_list,
    }
	#template = loader.get_template('index.html')
	#return HttpResponse(template.render(context, request))
	#return HttpResponse(video_list)
	return render(request, 'player/index.html', context)