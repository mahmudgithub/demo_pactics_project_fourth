#from django.shortcuts import render
#from .models import Board

#def home(request):
    # code suppressed for brevity

#def board_topics(request, pk):
  #  board = Board.objects.get(pk=pk)
   #s return render(request, 'topics.html', {'board': board})


from django.views.generic import ListView
from .models import post, most


class sos(ListView):
	model = post
	template_name = 'home1.html'
	context_object_name='app1'


class bos(ListView):
	model = most
	template_name = 'home2.html'
	context_object_name='app1'