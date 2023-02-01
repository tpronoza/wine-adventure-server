from wineadventureapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    uid = request.data['uid']

    user = User.objects.filter(uid=uid).first()

    if user is not None:
        data = {
            'id': user.id,
            'user_name': user.user_name,
            'uid': user.uid,
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)

@api_view(['POST'])
def register_user(request):

    user = User.objects.create(
        user_name=request.data['user_name'],
        uid=request.data['uid']
    )

    data = {
        'id': user.id,
        'user_name': user.user_name,
        'uid': user.uid,
    }
    return Response(data)
