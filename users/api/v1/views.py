# django
from django.contrib.auth.hashers import make_password

# rest_framework
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

# project
from ...models import User
from users.serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAdminUser])
def userInfo(request):
    '''
    유저(서비스 가입자)
    ---
    django admin에서 수정
    '''
    data = request.data
    # User Info (유저 정보)
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    # Register User 회원가입
    elif request.method == 'POST':
        try:
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                email=data['email'],
                password=make_password(data['password']),
                gender=data['gender'],
                bio=data['bio'],
            )
        except:
            message = {'detail': '이메일 혹은 유저네임이 중복되었습니다.'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    # Update User 업데이트
    elif request.method == 'PUT':
        user = request.user
        serializer = UserSerializer(user, many=False)
        user.first_name = data['first_name'],
        user.last_name = data['last_name'],
        user.email = data['email']
        user.bio = data['bio']

        if data['password'] != '':
            user.password = make_password(data['password'])

        user.save()

        return Response(serializer.data)
