from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['categories__name', 'tags__name']
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication for all actions

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        category = self.request.query_params.get('category')
        tag = self.request.query_params.get('tag')

        if category:
            queryset = queryset.filter(categories__name=category)

        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset



class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
