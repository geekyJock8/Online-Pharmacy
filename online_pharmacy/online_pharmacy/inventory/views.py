from django.http import HttpResponse
from django.apps import apps
from django.shortcuts import render


def showInventory(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id', False)
        item_name = request.POST.get('item_name', False)
        image = request.POST.get('image', False)
        otc_or_not = request.POST.get('otc_or_not', False)
        brand_name = request.POST.get('brand_name', False)
        salts = request.POST.get('salts', False)
        specifications = request.POST.get('specifications', False)
        category = request.POST.get('category', False)
        quantity = request.POST.get('quantity', False)
        price_per_item = request.POST.get('price_per_item', False)
        member = apps.get_model('items.item')
        b = member(item_id,item_name,image,otc_or_not,brand_name,salts,specifications,category)
        if b is not None:
             b.save()
        else:
            showInventory(request)
        #mem =  apps.get_model('inventory.sells')
        #c = mem(item_id,item_id,item_id,quantity,price_per_item)#pharmacy_id ka nahi pata
        #if c is not None:
            #c.save()
        #else:
            #showInventory(request)
        return HttpResponse('<h1> This is the Inventory page of the required pharmacy. </h1>')
    else:

        return HttpResponse('<h1> This is the Inventory page of the required pharmacy. </h1>')

def createInventory(request):
    return render(request,'inventory\create_inventory.html',{})