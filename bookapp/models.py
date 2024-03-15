from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return '{}'.format(self.name)



class Book(models.Model):
    title=models.CharField(max_length=200,null=True)

    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media')


# /// forgien key

    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.title)













# ///f&c


# class Book(models.Model):
#     title=models.CharField(max_length=200)
#     author=models.CharField(max_length=200)
#     price=models.IntegerField()
#
#     def __str__(self):
#         return '{}'.format(self.title)
