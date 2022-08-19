from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.serializers import TeamSerializer, PLayerSerializer, RegisterSerializer
from app.models import Team, Player
from rest_framework import generics
from rest_framework import permissions


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PLayerSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


# Create your views here.

def home(request):
    return HttpResponse("Ok")


def register(request):
    response = {"status": False}
    try:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            User.objects.create(username=username, email=email, password=password, first_name=first_name,
            last_name=last_name)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = {'message':"Your Account has successfully created", "status":True}
                return JsonResponse(response, status=201)
        else:
            response['message'] = "Method not allowed"

    except Exception as e:
        response['status'] = False
        response['error'] = repr(e)
        return JsonResponse(response)


def login(request):
    response = {"status": False}
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = {'message':"You are successfully Logged In", "status":True}
            else:
                response = {'message':"Username Or Password Is Not Correct"}

            return JsonResponse(response)
        else:
            response['message'] = "Method not allowed"

    except Exception as e:
        response['status'] = False
        response['error'] = repr(e)



def logout_view(request):
    logout(request)
