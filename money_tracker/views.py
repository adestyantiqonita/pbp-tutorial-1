from django.shortcuts import render
from money_tracker.models import TransactionRecord
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from money_tracker.forms import TransactionRecordForm
from django.urls import reverse


# Create your views here.

def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
        'list_of_transactions': transaction_data,
        'name': 'Qonita Adestyanti'
    }
    return render(request, "tracker.html", context)

def show_xml():
    data = TransactionRecord.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def create_transaction(request):
    form = TransactionRecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('money_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "create_transaction.html", context)

