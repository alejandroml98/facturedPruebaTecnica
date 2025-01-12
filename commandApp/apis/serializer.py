#DRF
from rest_framework import serializers

#Modelos
from .models import Tableros, Tareas

#enums
from .enums import EstadostareaEnum

class TablerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tableros
        fields = '__all__'
        read_only_fields = ["id"]

class TareasSerializer(serializers.ModelSerializer):
    def validate_estado(self, value):
        try:
            enum = EstadostareaEnum[value]
            return enum.value
        except Exception:
            raise serializers.ValidationError("Se debe elegir una opción valida [pendiente, en_progreso, completada]")
    class Meta:
        model = Tareas
        fields = '__all__'
        read_only_fields = ["id"]