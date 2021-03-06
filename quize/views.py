from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from .models import User, Contest, Category
from .forms import UserForm, CategoryForm, ContestForm

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
	title = "введите свой персональный код"
	args = {}
	args.update(csrf(request))
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			u = form.save()
			return redirect('add_cat', pk=u.id)
	else:
		form = UserForm()
		return render(request, 'quize/add_user.html', {'form': form, 'title':title})

def add_cat(request, pk):
	title = "выберите категорию конкурса"
	if request.method == "POST":
		form = CategoryForm(request.POST)
		user = get_object_or_404(User, pk=pk)
		print(request.POST)
		print(request.POST.get('cat'))
		if form.is_valid():
			cat = form.save(commit=False)
			cat.user = user
			cat.save()
			return redirect('add_cont', pk=cat.id)
		else:
			return redirect('/')
	else:
		form = CategoryForm()
		return render(request, 'quize/add_user.html', {'form': form, 'title':title})

def add_cont(request, pk):
	title = "введите название конкурса, выберите дату проведения и занятое место"
	if request.method == "POST":
		form = ContestForm(request.POST)
		cat = get_object_or_404(Category, pk=pk)
		print("------------------------------------")
		print (pk)
		print (cat.user.pk)
		print("------------------------------------")
		if form.is_valid():
			cont = form.save(commit=False)
			cont.cat = cat
			cont.save()
			
			#user = get_object_or_404(User, pk=cat.user.pk)
			return redirect('user_detail', pk=cat.user.pk)
	else:
		form = ContestForm()
		return render(request, 'quize/add_user.html', {'form': form, 'title':title})


def user_edit(request, pk):
	title = "введите свой персональный код"
	user = get_object_or_404(User, pk=pk)
	if request.method == "POST":
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			user = form.save()
			return redirect('user_detail', pk=user.pk)
	else:
		form = UserForm(instance=user)
		return render(request, 'quize/add_user.html', {'form': form, 'title':title})

def user_remove(request, pk):
	user = get_object_or_404(User, pk=pk)
	user.delete()
	return redirect('/')

def user_results(request):
	cont = Contest.objects.all()
	user = User.objects.all()
	return render(request, 'quize/results.html', {'cont':cont, 'user':user})
