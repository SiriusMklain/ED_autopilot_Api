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
            'short_text_en',
            'text_app_en',
            'short_text_instruction',
            'short_text_instruction_en',
            'text_instruction',
            'text_instruction_en',

        ]


class GlobalActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalActive
        fields = [
            'id',
            'global_active',
            'check_stat',
        ]


class CmndrSerializer(serializers.ModelSerializer):
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
            'global_activation',
        ]