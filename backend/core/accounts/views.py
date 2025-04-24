from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(APIView):
    def post(self, request):
       serializer = RegisterSerializer(data=request.data)
       if serializer.is_valid():
          user = serializer.save()
          return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
       username = request.data.get('username')
       password = request.data.get('password')
       user = authenticate(request, username=username, password=password)
       if user:
         login(request, user)
         return Response({'message': 'Logged in'}, status=status.HTTP_200_OK)
       return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request):
        logout(request)
        return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)

                                                                                                                                                class UserDetailView(APIView):
                                                                                                                                                    permission_classes = [IsAuthenticated]

                                                                                                                                                        def get(self, request):
                                                                                                                                                                serializer = UserSerializer(request.user)
                                                                                                                                                                        return Response(serializer.data)