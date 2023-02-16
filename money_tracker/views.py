from django.shortcuts import render
from money_tracker.models import TransactionRecord

# Create your views here.

def show_tracker(request):
    transaction_data = TransactionRecord.objects.all()
    context = {
        'list_of_transactions': transaction_data,
        'name': 'Qonita Adestyanti'
        {% for transaction in list_of_transactions %}
    <tr>
        <td>{{transaction.name}}</td>
        <td>{{transaction.type}}</td>
        <td>{{transaction.amount}}</td>
        <td>{{transaction.date}}</td>
        <td>{{transaction.description}}</td>
    </tr>
{% endfor %}
    }
    return render(request, "tracker.html", context)

