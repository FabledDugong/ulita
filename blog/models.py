from django.db import models

# models = DATABASEs, tables are called CLASSes,
# columns of the tables are called VARIABLEs


class Post(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title
