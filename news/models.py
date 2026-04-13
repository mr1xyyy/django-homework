from django.db import models

class News(models.Model):
    title = models.CharField('Nomi', max_length=255)
    anons = models.CharField('Anons', max_length=255)
    full_text = models.TextField('Maqola')
    date = models.DateTimeField('Nashr etilgan sana')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'