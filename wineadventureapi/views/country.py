from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wineadventureapi.models import Country

class CountryView(ViewSet):

    def retrieve(self, request, pk):
        country = Country.objects.get(pk=pk)
        serializer = CountriesSerializer(country)
        return Response(serializer.data)
    
    def list(self, request):
        countries = Country.objects.all()
        serializer = CountriesSerializer(countries, many = True)
        return Response(serializer.data)
    
    def  create(self, request):
        country = Country.objects.create(
            country_name=request.data["country_name"]
        )
        serializer = CountriesSerializer(country)
        return Response(serializer.data)
    
    def update(self, request, pk):
        country = Country.objects.get(pk=pk)
        country.country_name = request.data["country_name"]
        
        country.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'country_name')
