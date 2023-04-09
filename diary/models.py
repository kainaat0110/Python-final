from django.db import models

class Diary_entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Diary_entry #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural='entries'
    
