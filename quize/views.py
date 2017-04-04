from django.shortcuts import render, get_object_or_404
from .models import User, Kon, Vid

# Create your views here.
def post_list(request):
	konkurs = Kon.objects.all()
	user = User.objects.all()
	return render(request, 'quize/post_list.html', {'konkurs':konkurs, 'user':user})

def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	#vid = Vid.objects.filter(user=user)
	konkurs = Kon.objects.all()
	return render(request, 'quize/user_detail.html', {'user':user, 'konkurs':konkurs})