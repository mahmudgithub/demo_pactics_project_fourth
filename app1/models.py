from django.db import models

class post(models.Model):
	name = models.CharField(max_length=100)
	roll = models.IntegerField() #ForeignKey('auth.user',on_delete=models.CASCADE,)
	city = models.CharField(max_length=100)
	#country = models.CharField(max_length=100)
	#about = models.TextField()

	def __str__(self):
		return self.name



class most(models.Model):
    country = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
            return self.country