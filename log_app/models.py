from django.db import models

# Create your models here.
class page_data(models.Model):
    # username=models.CharField(max_length=250)
    # password=models.CharField(max_length=250)
    # email=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    salary=models.IntegerField(default = 0)
    bones=models.IntegerField(default = 0)
    def __str__(self):
        return self.name
# class MyBaseModel(models.Model):
#     common_field = models.CharField(max_length=100)

#     class Meta:
#         abstract = True

# class MySubModel(MyBaseModel):
#     specific_field = models.IntegerField()
    
# class BaseModel(models.Model):
#     common_field = models.CharField(max_length=100)

# class SubModel(BaseModel):
#     specific_field = models.IntegerField()