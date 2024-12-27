from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    phone = models.CharField(max_length=20)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.username) if self.username else "No Username"

class Child(models.Model):
    parent = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.name) if self.name else "No Name"

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.subject}, From {self.sender.username} to {self.recipient.username}"

    class Meta:
        ordering = ['is_read', '-created_at']
