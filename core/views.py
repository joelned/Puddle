from django.shortcuts import render
from .models import Category, OrderItem

# Create your views here.

def index(request): 
    ordered_items = OrderItem.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories, 
        'ordered_items': ordered_items,
    })


def contact(request): 
    return render(request, 'core/contact.html')


