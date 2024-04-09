from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import AccessToken


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        respObj = {
            "status": "success",
            "data": {
                "user_id": user.id,
            },
        }

        return Response(respObj, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class UserLoginApiView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user_name = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=user_name, password=password)
            if user:
                respObj = {
                    "status": "success",
                    "data": {
                        "access_token": str(AccessToken.for_user(user)),
                        "user": {
                            "user_id": user.id,
                            "username": user.username,
                            "full_name": f"{user.first_name} {user.last_name}",
                            "email": user.email,
                        },
                    },
                }
                return Response(respObj, status=status.HTTP_200_OK)
            else:
                respObj = {
                    "status": "fail",
                    "data": {"Invalid email or password"},
                }
        except ValidationError:
            respObj = {
                "status": "fail",
                "data": serializer.errors,
            }
        return Response(respObj, status=status.HTTP_403_FORBIDDEN)
