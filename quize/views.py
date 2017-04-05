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
		print (form)
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
		print("-----------------------------------")
		print(request.POST)
		print(request.POST.get('cat'))
		if form.is_valid():
			print("====================================")
			print(pk)
			cat = form.save(commit=False)
			cat.user = user
			cat.save()
			return redirect('add_cont', pk=cat.id)
		else:
			return redirect('add_cont', pk=cat.id)
	else:
		form = CategoryForm()
		return render(request, 'quize/add_user.html', {'form': form, 'title':title})

def add_cont(request, pk):
	title = "введите название конкурса, выберите дату проведения и занятое место"
	if request.method == "POST":
		form = ContestForm(request.POST)
		cat = get_object_or_404(Category, pk=pk)
		if form.is_valid():
			cont = form.save(commit=False)
			cont.cat = cat
			cont.save()
			return redirect('/')
	else:
		form = ContestForm()
		return render(request, 'quize/add_user.html', {'form': form, 'title':title})