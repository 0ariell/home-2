from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'is_worker']

    def create(self, validated_data):
        # Puedes manejar la creación del usuario aquí
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            is_worker=validated_data.get('is_worker', False)
        )
        user.set_password(validated_data['password'])  # Asegúrate de encriptar la contraseña
        user.save()
        return user
