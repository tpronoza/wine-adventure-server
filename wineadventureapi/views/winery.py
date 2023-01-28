from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wineadventureapi.models import Winery

class WineryView(ViewSet):

    def retrieve(self, request, pk):
        try:
            winery = Winery.objects.get(pk=pk)
            serializer = WinerySerializer(winery)
            return Response(serializer.data)
        except Winery.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        wineries = Winery.objects.all()
        serializer = WinerySerializer(wineries, many=True)
        return Response(serializer.data)

    def create(self, request):

        winery = Winery.objects.create(
            winery_name=request.data["winery_name"]
        )
        serializer = WinerySerializer(winery)
        return Response(serializer.data)

    def update(self, request, pk):

        winery = Winery.objects.get(pk=pk)
        winery.winery_name = request.data["winery_name"]
        winery.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        winery = Winery.objects.get(pk=pk)
        winery.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class WinerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Winery
        fields = ('id', 'winery_name', 'details')
