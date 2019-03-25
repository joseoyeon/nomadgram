from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updatae_at = models.DateTimeField(auto_now=True)
    
    #class 에 대한 부가 정보는 이렇게 써야 한다.
    class Meta:
        abstract = True

class Image(TimeStampModel):

    """ Image Model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,null=True, on_delete=models.CASCADE)

class Comment(TimeStampModel):
    """Comment Model"""
    message = models.TextField()
    creator = models.ForeignKey(user_models.User,null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image,null=True, on_delete=models.CASCADE)

class Like(TimeStampModel):
    """ Like Models """
    creator = models.ForeignKey(user_models.User,null=True,  on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True,on_delete=models.CASCADE)