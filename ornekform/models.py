from django.db import models

#Database oluşturma alanıdır.

#Aşağıda database'in özellikleri belirtilmiştir.
#Database tanımlanırken Id tanımlamaya gerek yoktur, django kendisi bir Id atar ve bu Id'ye primary key özelliği verir.

class OrnekFormDatabase(models.Model):
    name = models.CharField(max_length = 50, verbose_name ="name")
    email = models.CharField(max_length = 200, verbose_name ="email")
    service = models.CharField(max_length = 50, verbose_name="service")
    budget = models.CharField(max_length = 50, verbose_name="budget")
    message = models.TextField(max_length = 500, verbose_name="message")
    
#Bunları yazdıktan sonra, bu bilgileri admin panelinde göstermek için admin.py'de işlemleri yap.