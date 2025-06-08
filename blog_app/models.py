from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    author= models.ForeignKey("auth.user",on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title

## 1-1 Relationship
# 1 user can have only 1 profile ==>1
# 1 profile is associated to only 1 user ==>1
# OneToOneField () ==> Any model

## 1- M relationship
# 1 user can add M post ==> M
# 1 post is associated to only 1 user ==>1
# In django user ForeignKey () ==> Use  in Many side Model

## M-M relationship
# 1 Student can learn from M teachers ==> M
# 1 Teacher can teach M students ==> M
# ManyToManyField() ==> Any Place

