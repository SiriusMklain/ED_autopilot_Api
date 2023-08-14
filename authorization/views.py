import os

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *


MEDIA_ROOT = settings.MEDIA_ROOT


global active_register


class GetCmdr(APIView):
    def get(self, request, id_commander):
        queryset = Cmndr.objects.get(id=id_commander)
        value = CmndrSerializer(queryset, many=False)

        return Response(value.data)


class CheckActive(APIView):
    permission_classes = []

    def post(self, request):
        global active_register
        active_register = False
        user_name = request.data["username"]
        unique_number = request.data["unique_number"]

        try:
            queryset = Cmndr.objects.get(name_cmdr=user_name)
            if queryset.code_active == unique_number:
                queryset.active = True
                queryset.save()
                active_register = True
            else:
                queryset.active = False
                queryset.save()
                active_register = False
        except ObjectDoesNotExist:
            pass

        return Response(active_register)


class GetDescription(APIView):
    def get(self, request):
        queryset = Description.objects.get(status_update=True)
        value = DescriptionSerializer(queryset, many=False)

        return Response(value.data)


class CheckUpdate(APIView):
    def get(self, request):
        queryset = GlobalActive.objects.get(check_stat=True)
        value = GlobalActiveSerializer(queryset, many=False)

        return Response(value.data)
