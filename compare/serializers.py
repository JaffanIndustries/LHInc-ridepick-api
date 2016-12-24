from rest_framework import serializers

class estimateSerializer(serializers.Serializer):
    service = serializers.CharField(max_length=30)
    product_id = serializers.CharField(max_length=250)
    display_name = serializers.CharField(max_length=30)
    max_cost = serializers.CharField(max_length=10)
    min_cost = serializers.CharField(max_length=10)
    range_estimate = serializers.CharField(max_length=20)
    currency = serializers.CharField(max_length=10)
    duration = serializers.CharField(max_length=10)
    distance = serializers.CharField(max_length=10)