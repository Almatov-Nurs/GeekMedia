from rest_framework import serializers
from .models import Posts, Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'description', 'image')


class PostSerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(many=True)
    category = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ('id', 'title', 'description', 'image', 'category', 'created_date', 'created_date_time', 'articles')

    def get_category(self, post):
        return {"ru_title": post.category.ru_title, "en_title": post.category.en_title} if post.category else None


class PostsSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = "id title description image created_date created_date_time category".split()

    def get_category(self, post):
        return post.category.ru_title if post.category else None


class PostCreateSerializers(serializers.Serializer):
    title = serializers.CharField(min_length=0, max_length=100)
    description = serializers.CharField()