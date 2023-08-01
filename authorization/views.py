from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .serializers import *


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
                queryset.save()  # Save the changes to the database
                active_register = True
        except ObjectDoesNotExist:
            pass  # Handle the case when Cmndr object does not exist

        return Response(active_register)


# class CheckUpdate(APIView):
#     pass

