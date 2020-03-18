from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from slugify import slugify

User = get_user_model()
# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return "{}".format(self.name)

        class Meta:
            ordering = ['order',]

class ContactInfo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return  "{}".format(self.title)


class HomePage(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    background = models.ImageField(upload_to='background/')

    def __str__(self):
        return  "{}".format(self.title)

    def preview_image(self):
        return mark_safe(
            "<img src='{}' style='width:300px' />".format(
                self.background.url
            )
        )

class AboutPage(models.Model):
    title = models.CharField(max_length=255)
    background = models.ImageField(upload_to='background/')
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return  "{}".format(self.title)

    def preview_image(self):
        return mark_safe(
            "<img src='{}' style='width:300px' />".format(
                self.background.url
            )
        )


class Article(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(null=True,
                                 blank=True,
                                 max_length=255)
    image = models.ImageField(upload_to='blog/',
                              null=True, blank=True)
    author = models.ForeignKey(User,
                               null=True,
                               blank=True,
                               on_delete=models.DO_NOTHING)
    text = models.TextField()
    publish_date = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.title)
    
    class Meta:
        ordering = ('-publish_date',)


class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return '{}'.format(self.category_name)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 


class Post(models.Model):
    article_author = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Categories, null=False, blank=False, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(null=True, blank=True, max_length=255)
    body = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/',
                              null=True, blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(371,247)],
                                    format='JPEG',
                                    options={'quality': 90})
    image_thumbnail_slide = ImageSpecField(source='image',
                                    processors=[ResizeToFill(1172,502)],
                                    format='JPEG',
                                    options={'quality': 90})
    image_thumbnail_detail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(1171,607)],
                                    format='JPEG',
                                    options={'quality': 90})
    # image = models.FileField(null=True, blank=True)
    status = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)

    class Meta:
        ordering = ('-posted_on',)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title
    
    # def save(self):
	# 	#Opening the uploaded image
    #     im = Image.open(self.image)
    #     output = BytesIO()
    #     im = im.resize(100,100)   
    #     im.save(output, format='JPEG', quality=100)
    #     output.seek(0)

    #     self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
    #     super(Modify,self).save()


class Footer(models.Model):
    linkedin = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    #copyright
    copyright = models.CharField(max_length=255)

    def __str__(self):
        return "{} {} {}".format(self.copyright, self.facebook, self.youtube, self.linkedin)
