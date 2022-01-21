from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = Category
        fields = ("id","name","children")

    def get_children(self, obj):
        return CategorySerializer(obj.get_children(), many=True).data