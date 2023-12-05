from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')

    def __str__(self):
        return self.title
