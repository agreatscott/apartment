from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from purchases.models import Purchase

@login_required
def index(request):

	#get purchases from database
	#purchases = Purchase.objects.filter(user=request.user)
	purchases = Purchase.objects.all()

	context = {'purchases' : purchases}
	return render(request, 'purchases/index.html', context=context)



	
