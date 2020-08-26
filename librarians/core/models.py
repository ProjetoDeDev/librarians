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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField(null=True)
    description = models.TextField(null=True)
    matter = models.ForeignKey('Matter', on_delete=models.CASCADE)
    # file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
