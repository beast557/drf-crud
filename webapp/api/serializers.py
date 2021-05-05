from rest_framework import serializers
from webapp.models import Post



# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length = 100)
#     body = serializers.CharField(max_length=300)
#     author = serializers.CharField(max_length=100)
#     date = serializers.DateTimeField()

#     def create(self,validated_data):
#         return Post.objects.create(validated_data)
    
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.body = validated_data.get('body',instance.body)
#         instance.author = validated_data.get('author',instance.author)
#         instance.save()
#         return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','author','body']

