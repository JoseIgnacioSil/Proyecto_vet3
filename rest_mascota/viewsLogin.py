from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    var_username = data['username']
    var_password = data['password']
    
    try:
        var_user = User.objects.get(username = var_username)
    except User.DoesNotExist:
        return Response('Usuario Inválido')
    
    pass_valido = check_password(var_password, var_user.password)
    
    if not pass_valido:
        return Response('Password Incorrecta')
    
    token, created = Token.objects.get_or_create(user=var_user)
    return Response(token.key)
    
