#DRF
from rest_framework import serializers

#Modelos
from .models import Tableros, Tareas

#enums
from .enums import EstadostareaEnum


class TareasSerializer(serializers.ModelSerializer):
    def validate_estado(self, value):
        try:
            enum = EstadostareaEnum(value)
            return enum.value
        except Exception:
            raise serializers.ValidationError('Se debe elegir una opción valida ["pendiente", "en progreso", "completada"]')
    class Meta:
        model = Tareas
        fields = '__all__'
        read_only_fields = ["id"]

class TablerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tableros
        fields = '__all__'
        read_only_fields = ["id"]

class TableroConTareasSerializer(serializers.ModelSerializer):
    #Incluir los hijos como un serializador anidado
    tareas = TareasSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Tableros
        fields = '__all__'
        read_only_fields = ["id"]


class RabbitmqMessageSerializer(serializers.Serializer):
    metodo = serializers.CharField(max_length=50)
    tabla = serializers.CharField(max_length=100)
    tareas_data =  serializers.DictField(required = False)
    tableros_data = serializers.DictField(required = False)


