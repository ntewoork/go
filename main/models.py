from django.db import models

# Create your models here.

class feature(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class our(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    vid = models.FileField(upload_to='meida/')

    def __str__(self):
        return self.name
    
class text(models.Model):
    text = models.TextField()
    nomi = models.CharField(max_length=90)


    def __str__(self):
        return self.text
    
class sevice(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class work(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    title = models.CharField(max_length=90)

    def __str__(self):
        return self.name
    
class plan(models.Model):
    name = models.CharField(max_length=90)
    pul = models.CharField(max_length=90)
    title1 = models.CharField(max_length=90)
    title2 = models.CharField(max_length=90)
    title3 = models.CharField(max_length=90)
    title4 = models.CharField(max_length=90)
    title5 = models.CharField(max_length=90)
    title6 = models.CharField(max_length=90)
    title7 = models.CharField(max_length=90)

    def __str__(self):
        return self.name
    

class team(models.Model):
    name = models.CharField(max_length=90)
    rasm = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=90)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class team2(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    rasm = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
    
class answer(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()

    def __str__(self):
        return self.name
    
class questions(models.Model):
    ism = models.CharField(max_length=90)
    e_mail = models.CharField(max_length=90)
    tel = models.IntegerField()
    pro = models.TextField()

    def __str__(self):
        return self.ism
    
class by(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.text



