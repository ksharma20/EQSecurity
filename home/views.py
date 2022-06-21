from django.shortcuts import redirect, render
from apis.models import EQSecurity

# Create your views here.
def home(request):

    if request.method == 'POST':
        symbol = request.POST.get('stockPick')
        return redirect(f'/stock/{symbol}')

    eqsec = EQSecurity.objects.all()
    eqsec = [ str(i.symbol) for i in eqsec]

    context = {
        'eqsec': eqsec
    }
    return render(request, 'home.html', context)


def stock(request, pk):
    context = {
        'pk': str(pk)
    }
    return render(request, 'stock.html', context)