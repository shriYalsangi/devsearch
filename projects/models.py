import uuid
from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  demo_link = models.CharField(max_length=2000, null=True, blank=True)
  source_link = models.CharField(max_length=2000, null=True, blank=True)
  tags = models.ManyToManyField('Tag', blank=True)
  vote_total = models.IntegerField(default=0, null=True, blank=True)
  vote_ratio = models.IntegerField(default=0, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title

class Review(models.Model):
  VOTE_TYPE = (
    ('up', 'Up Vote'),
    ('down', 'Down Vote'),
  )
  VOTE_TYPE_DICT = {key: value for key, value in VOTE_TYPE}
  body = models.TextField(null=True, blank=True)
  value = models.CharField(max_length=200, choices=VOTE_TYPE)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.value
  
class Tag(models.Model):
  name = models.CharField(max_length=200)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name