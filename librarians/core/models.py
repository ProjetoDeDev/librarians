from django.db import models


class Tags(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Matter(models.Model):
    title = models.CharField(max_length=128)
    tags = models.ManyToManyField('Tags')
    contents = models.ForeignKey('Content', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titlep


class Content(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    description = models.TextField()
    # file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
