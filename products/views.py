from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import Product_form, product_raw_form
# Create your views here.

# Object Delete Method:



def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('../../')
    context = { "obj" : obj
    }
    return render (request, 'product/produt_delete.html', context)


# dynamic URL Method
def dynamic_look_view (request, id ):
    obj = get_object_or_404(Product, id=id)
    context = { "my_obj" : obj }
    print(context)
    return render (request, 'product/dynamicrouting.html', context)

# Create object Form method
def product_create_raw_form(request, *args, **kwargs):
    form = product_raw_form()
    if request.method=="POST":
        my_form = product_raw_form(request.POST)
        if my_form.is_valid():
            #print("now the data is good")
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = { "form" : form }
    return render (request, 'product/createform-formmethod.html', context)



# create object model method

def product_create_form(request, *args, **kwargs):
    form = Product_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Product_form()

    context = { "createform" : form }

    return render (request,'product/createform-modelmethod.html', context)

# this is for raw HTML form Method
#def product_create_form(request):
#    print(request)
#    if request.method =='POST':
#        my_context= request.POST.get('title')
#        print(my_context)
#    context={}
#    print(context)
    # Product.objects.create(title= my_context) # it wll insert value into database
#    return render(request, 'createform.html', context)

def home_view(request,*args, **kwargs):
    return render(request,"home.html", {})

def product_view(request,*args, **kwargs):
    my_context ={
     "my_product_name" : "Fruits Category",
     "my_product_price": 150,
     "my_product_list" : ['apple', 'banana','orange']
    }
    return render(request, "product/product.html", my_context)

def item_view(request,*args, **kwargs):
    return render(request, "product/item.html", {})

def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # method1
    #my_context = {
    # 'titel' : obj.title,
    # 'description': obj.description
    #}
    # method2
    my_context = {
    'object': obj
    }

    return render(request,"product/detail.html",my_context)
