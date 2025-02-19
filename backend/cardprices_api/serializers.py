# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Card

# create a serializer class
class CardSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Card
        fields = ('id', 'name', 'condition','year')
