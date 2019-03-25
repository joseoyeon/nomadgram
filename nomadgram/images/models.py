from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updatae_at = models.DateTimeField(auto_now=True)
    
    #class 에 대한 부가 정보는 이렇게 써야 한다.
    class Meta:
        abstract = True

class Image(TimeStampModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

class Like(TimeStampModel):

    message = models.TextField()