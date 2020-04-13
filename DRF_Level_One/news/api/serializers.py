from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import Article, Journalist


class ArticleModelSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    # author = JournalistModelSerializer(read_only=True)
    # author = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"

    def get_time_since_pub(self, object):
        pub_date = object.pub_date
        now = datetime.now()
        time_delta = timesince(pub_date, now)
        return time_delta

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data


class JournalistModelSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article_detail")
    # articles = ArticleModelSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=50)
#     title = serializers.CharField(max_length=120)
#     description = serializers.CharField(max_length=200)
#     body = serializers.CharField()
#     location = serializers.CharField(max_length=120)
#     pub_date = serializers.DateField()
#     is_active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be different from one another!")
#         return data
#
#     def validate_title(self, value):
#         if len(value) < 25:
#             raise serializers.ValidationError("Title must be contain 25 characters or more!")
#         return value
