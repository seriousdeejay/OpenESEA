from rest_framework import serializers
from .models import Subscription, Organisation

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'name', 'description', 'currency', 
                'amount', 'created_at', 'updated_at') #__all__ selects all fields


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'