from django.shortcuts import render
from django.http import HttpResponse
from .models import Bali_Offer,Carol_Image
# from .forms import Bali_Offer_Form, Carol_Image_Form


# Create your views here.

def bali_view(request,*args,**kwargs):
#    obj  = Bali_Offer.objects.get(bali_offer_id=1)
#    obj1 = Carol_Image.objects.get(carol_image_id=1)
    obj = Bali_Offer.objects.get(bali_offer_featured='True')
    obj1 = Carol_Image.objects.get(carol_image_featured='True')
    my_context = { "offer" : obj , "carol" : obj1 }
    return render(request, 'bali/bali.html', my_context  )
