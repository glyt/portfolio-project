from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    #display the title in the admin page
    def __str__(self):
        return self.title

    #display the first 94 letters of the body
    def summary(self):
        return self.body[:94]

    #changed the display of the blog date
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

