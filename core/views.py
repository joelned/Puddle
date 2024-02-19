from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, OrderItem
from .forms import SignUpForm
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
 

def get_item(request, pk): 
    item = get_object_or_404(OrderItem, pk=pk)
    related_items=OrderItem.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'core/details.html', {
        'item': item, 
        'related_items': related_items,
    })

def signup(request):
    if request.method == "POST": 
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login")
    else:
        form =SignUpForm()
    

    return render(request, 'core/signup.html',{
        'form': form
    })


