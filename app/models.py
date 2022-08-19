from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=250, unique=True)
    total_player = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    i_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    i_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Team: {self.i_team.name}, User: {self.i_user.username}"

    def save(self, *args, **kwargs):
        if self.i_team.total_player > 2 :
            raise ValueError("A Team Cannot have more than 3 player")
        else:
            self.i_team.total_player += 1
            self.i_team.save()
            return super().save(*args, **kwargs)
