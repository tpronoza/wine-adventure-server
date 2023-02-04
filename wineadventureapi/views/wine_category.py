
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wineadventureapi.models import Wine_Category, Category, Wine

class WineCategoryView(ViewSet):

    # def retrieve(self, request, pk):
    #     """Handle GET request for single campaign"""
    #     try:
    #         wine_category = Wine_Category.objects.get(pk=pk)
    #         serializer = Wine_CategorySerializer(wine_category)
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET request for single campaign"""
        wine_category = Wine_Category.objects.all()
        serializer = Wine_CategorySerializer(wine_category, many = True)
        return Response(serializer.data)

    def  create(self, request):
        """Handle GET request for single campaign"""
        category = Category.objects.get(pk=request.data["category_id"])
        wine = Wine.objects.get(pk=request.data["wine_id"])
        wine_category = Wine_Category.objects.create(
            category = category,
            wine = wine
        )
        serializer = Wine_CategorySerializer(wine_category)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handle GET request for single campaign"""
        wine_category = Wine_Category.objects.get(pk=pk)
        wine_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class Wine_CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Wine_Category
        fields = ('id', 'category_id', 'wine_id')
        depth = 2
