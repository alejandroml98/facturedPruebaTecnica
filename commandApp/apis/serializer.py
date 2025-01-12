#DRF
from rest_framework import serializers

#Modelos
from .models import Tableros, Tareas


class TablerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tableros
        fields = '__all__'
        read_only_fields = ["id"]