from django.shortcuts import render

from .models import Product
# Create your views here.

def product_detail_view(request):
	obj = Product.objects.get(id=1)

	# context = {
	# 	'name': obj.name,
	# 	'description': obj.description,
	# 	'price': obj.price,
	# 	'summary': obj.summary,
	# 	'featured': obj.featured,
	# }

	context = {
		'obj': obj,
	}
	
	return render(request, 'product/details.html', context)