from rest_framework import serializers
from actor.models import Actor
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__' 
