import uuid
from django.db import models
from users.models import Profile

class Project(models.Model):
  owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
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
  
  @property
  def getVoteCount(self):
    reviews = self.review_set.all()
    upVotes = reviews.filter(value='up').count()
    totalVotes = reviews.count()
    ratio = (upVotes / totalVotes) * 100
    self.vote_total = totalVotes
    self.vote_ratio = ratio
    self.save()
  
  class Meta:
    ordering = ['-vote_ratio', '-vote_total', 'title']
  
  @property
  def reviewers(self):
    queryset = self.review_set.all().values_list('owner__id', flat=True)
    return queryset

class Review(models.Model):
  VOTE_TYPE = (
    ('up', 'Up Vote'),
    ('down', 'Down Vote'),
  )
  VOTE_TYPE_DICT = {key: value for key, value in VOTE_TYPE}
  body = models.TextField(null=True, blank=True)
  value = models.CharField(max_length=200, choices=VOTE_TYPE)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    unique_together = [['owner', 'project']]

  def __str__(self):
    return self.value
  
class Tag(models.Model):
  name = models.CharField(max_length=200)
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name