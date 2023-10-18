from rest_framework import serializers
from .models import *


class USERSerializer(serializers.ModelSerializer):
    class Meta:
        model=USER
        fields = "__all__"