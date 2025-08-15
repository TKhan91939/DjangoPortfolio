from django.db import models

# Create your models here.
class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    img = models.ImageField(upload_to="devs/")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        managed = True
        verbose_name = "Developer"
        verbose_name_plural = "Developers"





class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    img = models.ImageField(upload_to="projects/")
    date = models.DateField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)
    gist = models.CharField(max_length=100, null=True, blank=True)
    git_id = models.IntegerField(unique=True, null=True, blank=True)
    dev = models.ManyToManyField(Developer, related_name="developers")

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        verbose_name = "Project"
        verbose_name_plural = "Projects"

# List display 
# Jazmin 
# drf
