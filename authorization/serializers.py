from rest_framework import serializers
from .models import *


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            'id',
            'status_update',
            'version_app',
            'short_text',
            'text_app',
        ]


class GlobalActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalActive
        fields = [
            'id',
            'global_active'
        ]


class CmndrSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer(required=False)
    global_activation = GlobalActiveSerializer(required=False)

    class Meta:
        model = Cmndr
        fields = [
            'name_cmdr',
            'code_active',
            'active',
            'monitor',
            'screen_size',
            'keyboard_layout',
            'description',
            'global_activation',
        ]