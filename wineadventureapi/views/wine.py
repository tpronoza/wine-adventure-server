from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wineadventureapi.models import Wine,Wine_Category, Category, User

class WineView(ViewSet):

    def retrieve(self, request, pk):
        wine = Wine.objects.get(pk=pk)
        serializer = WineSerializer(wine)
        return Response(serializer.data)

    def list(self, request):
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["user"])

        wine = Wine.objects.create(
            wine_name=request.data["wine_name"],
            year_produced=request.data["year_produced"],
            wine_picture=request.data["wine_picture"],
            description=request.data["description"],
            wine_type=request.data["wine_type"],
            price=request.data["price"],
            favorite=request.data["favorite"],
            wish_list=request.data["wish_list"],
            wine_list=request.data["wine_list"],
            country_name=request.data["country_name"],
            user=user
        )
        for id in request.data["winecategory"]:
            category_id = Category.objects.get(pk=id)
            Wine_Category.obectes.create(category_id=category_id, wine_id = wine)
        serializer = WineSerializer(wine)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["user"])

        wine = Wine.objects.get(pk=pk)
        wine.wine_name=request.data["wine_name"]
        wine.year_produced=request.data["year_produced"]
        wine.wine_picture=request.data["wine_picture"]
        wine.description=request.data["description"]
        wine.wine_type=request.data["wine_type"]
        wine.price=request.data["price"]
        wine.favorite=request.data["favorite"]
        wine.wish_list=request.data["wish_list"]
        wine.wine_list=request.data["wine_list"]
        wine.country_name=request.data["country_name"]
        wine.user=user
        wine.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        wine = Wine.objects.get(pk=pk)
        wine.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class WineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine_Category
        depth = 1
        fields = ('category_id', 'wine_id')

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id', 'wine_name', 'year_produced', 'wine_picture', 'description', 'wine_type', 'price', 'favorite', 'wish_list', 'wine_list', 'country_name', 'user')
        depth = 1
