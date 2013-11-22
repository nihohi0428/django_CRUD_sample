from django.db import models

# Create your models here.
class Record(models.Model):
    username = models.CharField(max_length=200)
    description = models.TextField()
    score = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all(kls):
        return kls.objects.all()

    @classmethod
    def get_records_by_username(kls, name):
        return kls.objects.filter(username__exact = name)
    
       