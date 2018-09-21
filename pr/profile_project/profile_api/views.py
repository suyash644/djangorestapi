from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    def get(self,request, format=None):
        """ Return a list of APIView fetures """
        an_api = ['suyash',
        'nitesg',
        'okself',
        'nothing']
        return Response({"message":'Hello!',"an_api":an_api})
