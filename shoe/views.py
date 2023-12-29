from django.shortcuts import render, redirect
from shoe.forms import ShoeForm
from shoe.models import Shoe, Checkout

from django.shortcuts import render, redirect
from shoe.models import Checkout
from shoe.models import Shoe
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient


# Create your templates here.


# Create your views here.


# .save() is the ORM equivalent of the SQL insert to statement.
def show(request):
    shoes = Shoe.objects.all()
    return render(request, "show.html", {'shoes': shoes})


def shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ShoeForm()
    return render(request, 'index.html', {'form': form})


# .all() is the ORM equivalent of the SQL statement "SELECT * FROM tablename"


# .get is the ORM equivalent of the SQL statement "SELECT * FROM tablename WHERE id = ? "
# method update carries the update process for a single record

def edit(request, id):
    shoe = Shoe.objects.get(id=id)
    return render(request, 'edit.html', {'shoe': shoe})


def update(request, id):
    shoe = Shoe.objects.get(id=id)
    form = ShoeForm(request.POST, instance=shoe)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'shoe': shoe})


# .delete() is the ORM equivalent of the statement SQL : " DELETE FROM tablename WHERE id = ? "
def destroy(request, id):
    shoe = Shoe.objects.get(id=id)
    shoe.delete()
    return redirect("/show")


def checkout(request, id):
    shoes = Shoe.objects.get(id=id)
    return render(request, "checkout.html", {'shoes': shoes})


def checkoutpay(request, id):
    shoes = Shoe.objects.get(id=id)
    if request.method == "POST":

        # capture input
        amount = shoes.shoe_price
        phoneNumber = request.POST.get('contact')

        # validation on the entries
        if not phoneNumber or not phoneNumber.isdigit():
            return HttpResponse("invalid phone number")
        if not amount or not amount.isdigit():
            return HttpResponse("invalid phone number")
        # Mpesa processes
        cl = MpesaClient()
        phone_number = int(phoneNumber)
        amount = int(amount)
        account_reference = 'CELESTIN ENTERPRISES'
        transaction_desc = 'Evanicela Payment'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
        return render(request, "checkout.html", {'shoes': shoes})
