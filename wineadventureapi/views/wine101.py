from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wineadventureapi.models import Wine101, User

class Wine101View(ViewSet):

    def retrieve(self, request, pk):
        wine101 = Wine101.objects.get(pk=pk)
        serializer = Wine101Serializer(wine101)
        return Response(serializer.data)

    def list(self, request):
        wines101 = Wine101.objects.all()
        serializer = Wine101Serializer(wines101, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["id"])

        wine101 = Wine101.objects.create(
            article_name=request.data["article_name"],
            context=request.data["context"],
            article_image=request.data["article_image"],
            article_link=request.data["article_link"],
            user=user
        )
        serializer = Wine101Serializer(wine101)
        return Response(serializer.data)

    def update(self, request, pk):

        user = User.objects.get(pk=request.data["id"])

        wine101 = Wine101.objects.get(pk=pk)
        wine101.article_name=request.data["article_name"]
        wine101.context=request.data["context"]
        wine101.article_image=request.data["article_image"]
        wine101.article_link=request.data["article_link"]
        wine101.user=user
        wine101.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        wine101 = Wine101.objects.get(pk=pk)
        wine101.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class Wine101Serializer(serializers.ModelSerializer):

    class Meta:
        model = Wine101
        fields = ('id', 'article_name', 'context', 'article_image', 'article_link', 'user')
        depth = 1
