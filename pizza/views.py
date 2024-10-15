from django.shortcuts import render, redirect
from .models import Pizza
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def homePage(request):
    return render(request, "Index.html")


def orderPage(request):
    form_pk = None
    form = OrderForm
    if request.method == 'POST':
        filled_form = OrderForm(request.POST)
        if filled_form.is_valid():
            messages.success(request, "Your order successfully Placed")
            status = True
            saved_form = filled_form.save()
            form_pk = saved_form.id
        else:
            messages.error(request, "Try again...")
            status = False
        return render(request, "OrderPage.html", {'form': form,'status': status, 'form_pk': form_pk})

    else:
        return render(request, "OrderPage.html", {'form': form})


def editPage(request, pk):
    note = ''
    status = False
    Data = Pizza.objects.get(pk=pk)
    form = OrderForm(instance=Data)
    if request.method == 'POST':
        edit_form = OrderForm(request.POST, instance=Data)
        if edit_form.is_valid():
            edit_form.save()
            note = "Your information is successfully Edited"
            status = True
        else:
            note = "Try Again"
            status = False

    return render(request, "EditPage.html", {'form': form, 'note': note, 'status': status, 'pk': pk})


def informationPage(request):
    information = Pizza.objects.all()
    return render(request, "InformationPage.html", {'information': information})


def delete(request, id):
    Data = Pizza.objects.get(id=id)
    Data.delete()
    return redirect('information')