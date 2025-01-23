from django.db import models

# Create your models here.
# class Discount_Log(models.Model):
#     report = models.ForeignKey(Report, on_delete=models.CASCADE,related_name='discount_report')
#     discount= models.DecimalField(max_digits=3, decimal_places=1,default=0)
#     dis_reason=models.CharField(max_length=500,default='',null=True)
#     dis_dt=models.DateTimeField(auto_now_add=True)
#     dis_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='discount_report_user',null=True)
    

class sentence(models.Model):
    sentence = models.CharField(max_length=5000)
    learning_type = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    tone = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    order = models.CharField(max_length=100)

class word(models.Model):
    word = models.CharField(max_length=100)
    
    