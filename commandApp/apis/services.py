from .serializer import RabbitmqMessageSerializer


def rabbitmq_data_transform(metodo, tabla, tableros_data, tareas_data):
    rabbitmq_data = {
        "metodo": metodo,
        "tabla": tabla,
        "tableros_data": tableros_data,
        "tareas_data": tareas_data
    }
    rabbitmq_serializer = RabbitmqMessageSerializer(rabbitmq_data)
    return rabbitmq_serializer.data