from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=10000)
    img_url= models.URLField(null=True, max_length=800)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'    
