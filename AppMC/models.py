from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='staic/usuario.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
                                .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
                                .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(upload_to="productos", null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]