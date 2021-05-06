from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from webapp.models import Post
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt


# api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class-bassed view
from rest_framework.views import APIView

#Generic views
from rest_framework import generics
from rest_framework import mixins

# token auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GenericPostView(
generics.GenericAPIView,
mixins.ListModelMixin,
mixins.CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class GenericPostsView(
generics.GenericAPIView,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin
):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        return self.retrieve(request)

    def put(self, request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)

class ListPosts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post():
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetails(APIView):
    def get_object(self,id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self,request,id):
        post = self.get_object(id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_200_OK)


# function based views
@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)


@api_view(['POST'])
def post_create(request):

    if request.method ==   'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT','DELETE'])
def post_detail_pk(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return Response(serializer.data)
        

    if request.method == 'POST':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_200_OK)