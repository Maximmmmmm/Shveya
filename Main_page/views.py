from django.shortcuts import render

# Create your views here.
def show_home(request):

	return render(request, 'Main_page/home.html', context={"home": 'this is home page'})
