from django.db import models
import datetime


# creating the editor models
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()
#creating the tags model
class tags(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name

#creating the Article model
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    


    
   
   