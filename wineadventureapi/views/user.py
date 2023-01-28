from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from.user import User

class UserView(ViewSet):

    def retrieve(self, request, pk):

        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def list(self, request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'uid')
