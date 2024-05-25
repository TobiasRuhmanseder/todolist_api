from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','titel', 'description', 'created_at'] # , user