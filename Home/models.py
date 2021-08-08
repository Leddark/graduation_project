from django.db import models

# Create your models here.


class Sign_Up (models.Model):
    
    fullname = models.CharField(max_length=150 , blank=False , db_column="الاسم كامل" , verbose_name="الاسم كامل" , null=True)
    User = models.CharField(max_length=70 , unique=True , blank=False , db_column="اسم المستخدم" , verbose_name="اسم المستخدم", null=True)
    
    email = models.EmailField(unique=True , blank=False , db_column="البريد الاكتروني" , verbose_name="البريد الاكتروني", null=True)
    
    password = models.CharField(max_length=50 , blank=False , db_column="كلمة السر" , verbose_name="كلمة السر", null=True)
    Retype_password = models.CharField(max_length=50 , blank=False , db_column="اعد ادخال كلمة السر" , verbose_name="اعد ادخال كلمة السر", null=True)


    def __str__(self):
        return self.fullname 
    class Meta:	
        db_table = 'مستخدمين'
        ordering = ['id']	



