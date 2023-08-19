from django.db import models


class Advertisement(models.Model):
    title = models.CharField('название', max_length=100)
    description = models.CharField('описание', max_length=500)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='уместен ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, price = {self.price})'

    class Meta:
        db_table = 'advertisement'
