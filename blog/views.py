from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import CommentCreateSerializer, PostDetailSerializer, PostListSerializer


class PostListView(APIView):

    def get(self, request):
        # getting all active posts
        posts = Post.objects.filter(moderation=False)
        # many records to serializer
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):

    def get(self, request, pk):
        posts = Post.objects.get(id=pk, moderation=False)
        serializer = PostDetailSerializer(posts)
        return Response(serializer.data)


class CommentCreateview(APIView):

    def post(self, request):
        # pass data from client request to comment
        comment = CommentCreateSerializer(data=request.data)
        # check comment on validity and save if valid
        if comment.is_valid():
            comment.save()
        return Response(status=201)