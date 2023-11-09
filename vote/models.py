from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='candidates/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name} in {self.position.name}" 