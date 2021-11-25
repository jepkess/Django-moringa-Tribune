from django.db import models
import datetime 
import datetime as dt


# creating the editor models
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    #blank=true allows us to add null values to our database.

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
    article_image=models.ImageField(upload_to='articles/')

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

     #class method that will query the database and fetch the results.
    @classmethod 
    def search_by_title(cls,search_term):# search_by_title method filter all the artcle in the database and return the one which matches with the search results.
        news = cls.objects.filter(title__icontains=search_term)
        return news

     
    


    
   
   