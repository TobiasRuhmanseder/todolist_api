from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email'] 

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer() ##custom data
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault()) ## directly from rest_framework
    class Meta:
        model = Todo
        fields = ['id','title', 'description', 'created_at', 'user', 'time_passed'] 