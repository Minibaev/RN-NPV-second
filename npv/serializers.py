from rest_framework.serializers import Serializer
from rest_framework.serializers import IntegerField, FloatField


class InputSerializer(Serializer):
    year = IntegerField()
    coeff = FloatField()
