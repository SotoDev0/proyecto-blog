from rest_framework import serializers
from categorias.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','slug','description','published']
        