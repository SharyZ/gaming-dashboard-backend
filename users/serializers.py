from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your serializers here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'userimage', )
