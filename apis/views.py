from django.shortcuts import redirect
import pandas as pd
from dateutil import parser
from .models import EQSecurity, Bhavcopy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EQSecuritySer, BhavcopySer, models


# Create your views here.
def refresh(request):
    
    eqsecurity= pd.read_csv('https://archives.nseindia.com/content/equities/EQUITY_L.csv')
    for row in eqsecurity.itertuples():
        date = parser.parse(str(row[4]))
        # print(f' Symbol={row[1]}, Name={row[2]} \t Series={row[3]} \t Date={date} \t Value={row[5]} \t ISIN={row[7]} ')
        _, created= EQSecurity.objects.get_or_create(symbol=str(row[1]), name=str(row[2]), series=str(row[3]), date=date, value=int(row[5]), isin=str(row[7]))


    bhavcopy= pd.read_csv('https://archives.nseindia.com/products/content/sec_bhavdata_full_20062022.csv')
    bhavcopy[" DELIV_QTY"].replace('-', 0, regex=True, inplace=True)
    bhavcopy[" DELIV_PER"].replace('-', 0, regex=True, inplace=True)
    for row in bhavcopy.itertuples():
        try:
            symbol = EQSecurity.objects.get(symbol=f'{row[1]}')
            # print(f' symbol={symbol}, series={row[2]}, date={row[3]}, prev_close={row[4]}, open_price={row[5]}, high_price={row[6]}, low_price={row[7]}, last_price={row[8]}, close_price={row[9]}, avg_price={row[10]}, ttl_qnty={row[11]}, turnover={row[12]}, trades={row[13]}, deliv_qty={row[14]}, deliv_per={row[15]} ')
            date = parser.parse(str(row[3]))
            _, created= Bhavcopy.objects.get_or_create(symbol=symbol, series=str(row[2]), date=date, prev_close=float(row[4]), open_price=float(row[5]), high_price=float(row[6]), low_price=float(row[7]), last_price=float(row[8]), close_price=float(row[9]), avg_price=float(row[10]), ttl_qnty=int(row[11]), turnover=float(row[12]), trades=int(row[13]), deliv_qty=int(row[14]), deliv_per=float(row[15]))

        except Exception as e:
            print(f"*************************** ERROR: {e} ******************************************")
            print(f' symbol={row[1]}, series={row[2]}, date={row[3]}, prev_close={row[4]}, open_price={row[5]}, high_price={row[6]}, low_price={row[7]}, last_price={row[8]}, close_price={row[9]}, avg_price={row[10]}, ttl_qnty={row[11]}, turnover={row[12]}, trades={row[13]}, deliv_qty={row[14]}, deliv_per={row[15]} ')
          

    return redirect('/')


@api_view(['GET'])
def stock(request, pk):
    symbol = EQSecuritySer(models.EQSecurity.objects.get(symbol=pk))
    return Response(symbol.data)

@api_view(['GET'])
def bhav(request, pk):
    try:
        stock = BhavcopySer(models.Bhavcopy.objects.get(symbol=models.EQSecurity.objects.get(symbol=pk)))
        return Response(stock.data)
    except Exception as e:
        return Response({ 'error': e, 'Date': False})