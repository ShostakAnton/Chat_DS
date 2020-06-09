# перевод с одного типа даных в другой
# serializers позволяет полученые данные из базы данных обработать и показать в json формате

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chat, Room


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""

    creater = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("creater", "invited", "date")