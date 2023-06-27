from django.shortcuts import redirect, render
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse
def index(request):
    products=Product.objects.all()
   
    
    # params={'no_of_slides':nSlides, 'range':range(1,nSlides),'product':products}
    # allProds=[[products,range(1,nSlides),nSlides],
    #           [products,range(1,nSlides),nSlides]]
    allProds=[]
    catprods=Product.objects.values('product_category','id')
    cats={item['product_category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(product_category=cat)
        n=len(products)
        nSlides = n//4 + ceil((n/4 )- (n//4))
        allProds.append([prod,range(1,nSlides),nSlides])


    return render(request,'shop/index.html',{'allProds':allProds})


def searchMatch(query,item):
      if query in item.product_description.lower() or query in item.product_name.lower() or query in item.product_category.lower():
        return True
      else:
        return False
  
def search(request):
      query=request.GET.get('search')
      
      allProds=[]
      catprods=Product.objects.values('product_category','id')
      cats={item['product_category'] for item in catprods}
      for cat in cats:
        prodtemp=Product.objects.filter(product_category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
      params = {'allProds': allProds, "msg": ""}
      if len(allProds) == 0 or len(query)<2:
        params={'msg':"Please make sure to enter relevant search query"}
        
      return render(request, 'shop/index.html', params)



        # n=len(prod)
        # nSlides = n//4 + ceil((n/4 )- (n//4))
        # if len(prod)!= 0:
        #   allProds.append([prod,range(1,nSlides),nSlides])

        # params={'allProds':allProds,"msg":""}
        # if len(allProds)==0 or len(query)<4:
        #  params={'msg':"Please make sure to enter relevant search query"} 
        # return render(request,'shop/search.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    thank = False
    if request.method=="POST":
       name=request.POST.get('name','')
       email=request.POST.get('email','')
       phone=request.POST.get('phone','')
       desc=request.POST.get('desc','')
       contact=Contact(name=name,email=email,phone=phone,desc=desc)
       contact.save()
       thank = True
    return render(request,'shop/contact.html',{'thank':thank})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def productview(request,myid):
     #fetch the product using id
     product=Product.objects.filter(id=myid)
     
     return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        order=Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The Order Has Been Placed.")
        update.save()
        thank = True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})


      
    return render(request,'shop/checkout.html')

