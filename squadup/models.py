from django.db import models



# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=20)

    def __str__(self):
        return self.username

        
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    image = models.TextField()
    user = models.ForeignKey(User, null= True, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_comment ='user_comment'
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, null= True, on_delete=models.CASCADE, related_name='user_comment')

    def __str__(self):
        return self.user_comment

