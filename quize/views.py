from django.shortcuts import render, get_object_or_404
from .models import User, Contest, Category
from .forms import UserForm

# Create your views here.
def post_list(request):
	cont = Contest.objects.all()
	user = User.objects.all()
	return render(request, 'quize/post_list.html', {'cont':cont, 'user':user})

def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	cont = Contest.objects.all()
	return render(request, 'quize/user_detail.html', {'user':user, 'cont':cont})

def add_user(request):
	form = UserForm()
	return render(request, 'quize/add_user.html', {'form': form})