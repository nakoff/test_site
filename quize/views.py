from django.shortcuts import render
from .models import User, Kon

# Create your views here.
def post_list(request):
	konkurs = Kon.objects.all()
	return render(request, 'quize/post_list.html', {'konkurs':konkurs})