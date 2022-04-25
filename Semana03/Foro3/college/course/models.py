from django.db import models

# model Caterory
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# model Course
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, 
                on_delete=models.CASCADE,
                blank=True,
                null=True,
                related_name='Category')
    def __str__(self):
        return self.title

