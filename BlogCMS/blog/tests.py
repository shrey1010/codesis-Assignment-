from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import BlogPost

class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.post1 = BlogPost.objects.create(
            title='Test Post 1',
            content='Content for Test Post 1',
            author='Author 1'
        )
        self.post2 = BlogPost.objects.create(
            title='Test Post 2',
            content='Content for Test Post 2',
            author='Author 2'
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_blog_posts(self):
        url = '/api/posts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_blog_post(self):
        url = f'/api/posts/{self.post1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post 1')

    def test_create_blog_post(self):
        url = '/api/posts/'
        data = {
            'title': 'New Post',
            'content': 'Content for New Post',
            'author': 'Author 3'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 3)

    def test_update_blog_post(self):
        url = f'/api/posts/{self.post1.id}/'
        data = {
            'title': 'Updated Title'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.title, 'Updated Title')

    def test_delete_blog_post(self):
        url = f'/api/posts/{self.post2.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 1)
