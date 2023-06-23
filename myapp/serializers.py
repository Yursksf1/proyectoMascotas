from rest_framework import serializers
from .models import Pet, Specie, Person

class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    # specie = SpecieSerializer()

    class Meta:
        model = Pet
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'