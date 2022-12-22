from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Seller
from .models import Product

# Create your views here.

tem_path = 'sellers/'

class IndexView(generic.ListView):
    template_name = tem_path + 'index.html'
    context_object_name = 'latest_seller_list'
    
    def get_queryset(self):
        return Seller.objects.filter(regist_date__lte = timezone.now()).order_by('-regist_date')[:5]

class DetailView(generic.DetailView):
    model = Seller
    template_name = tem_path + 'detail.html'
    
    def get_queryset(self):
        return Seller.objects.filter(regist_date__lte = timezone.now())
    
class ResultsView(generic.DetailView):
    model = Seller
    template_name = tem_path + 'results.html'
    
    def get_queryset(self):
        return Seller.objects.filter(regist_date__lte = timezone.now())
    
def add(request, seller_id):
    seller = get_object_or_404(Seller, pk = seller_id)
    try:
        selected_product = seller.product_set.get(pk = request.POST['product'])
    except (KeyError, Product.DoesNotExist):
        # Redisplay the product add form.
        return render(request, 'sellers/detail.html', {
            'seller': seller,
            'error_message': "You didn't select a product.",
        })
    else:
        selected_product.item_quantity += 1
        selected_product.save()
        return HttpResponseRedirect(reverse('sellers:results', args = (seller_id,)))
        




# def detail(request, item_id):
#     return HttpResponse("You're looking at product %s." % item_id)

# def results(request, item_id):
#     response = "Yor're looking at the results of product %s."
#     return HttpResponse(response % item_id)

# def add(request, item_id):
#     return HttpResponse("You're add quantity product %s." %item_id)