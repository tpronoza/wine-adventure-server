from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from.profile import Profile

class ProfileView(ViewSet):

    def retrieve(self, request, pk):

        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def list(self, request):

        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'profile_image', 'about_me', 'favorite', 'wish_list', 'my_wine_list', 'uid')
