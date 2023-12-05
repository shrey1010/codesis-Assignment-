from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Include specific fields if needed

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'  # Include specific fields if needed

class BlogPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'publication_date', 'categories', 'tags']
