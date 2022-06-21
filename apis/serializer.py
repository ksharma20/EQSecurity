from rest_framework import serializers
from . import models


class BhavcopySer(serializers.ModelSerializer):
    class Meta:
        model = models.Bhavcopy
        fields = [
            'symbol','series','date','prev_close','open_price','high_price','low_price','last_price','close_price','avg_price','ttl_qnty','turnover','trades','deliv_qty','deliv_per'
        ]

class EQSecuritySer(serializers.ModelSerializer):
    bhavs = BhavcopySer(many=True, read_only=True)
    class Meta:
        model = models.EQSecurity
        fields = [
            'symbol','name','series','date','value','isin', 'bhavs'
        ]
