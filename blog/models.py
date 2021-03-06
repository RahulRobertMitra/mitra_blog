from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    """
    Represents a blog post
    """

    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'DRAFT'),
        (PUBLISHED, 'PUBLISHED')
    ]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        null=False
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible'
    )

    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )

    slug = models.SlugField(
        null=False,
        unique_for_date='published',
    )

    def __str__(self):
        return self.title

class Meta:
    ordering = ['-created']

class CommentSection(models.Manager):

    def approved(self):
        return self.filter(approved=True)

class Comment(models.Model):
    """
    represents a comment on a blog post
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )

    name = models.TextField(max_length=50, null=False)
    email = models.EmailField(null=False)
    text = models.TextField(max_length=255, null=False)
    approved = models.BooleanField(default=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    objects = CommentSection()



    def str(self):
        return self.name + self.text

    class Meta:
        ordering = ['-created']
