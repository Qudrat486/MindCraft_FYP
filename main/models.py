from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Category(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def get_all_category(self):
        return Category.objects.all().order_by('id')
    
    

class Author(models.Model):
    author_profile = models.ImageField(upload_to="Media/author")
    name = models.CharField(max_length=100, null=True)
    about_author= models.TextField()
    
    def __str__(self):
        return self.name
    

class Level(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )
    
    featured_image = models.ImageField(upload_to="Media/featured_img", null=True)
    featured_video = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    price = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True)
    slug = models.SlugField(default='',max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)
    
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("course_details", kwargs={"slug": self.slug})
    
    
def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Course.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if  exists:
        new_slug= "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Course)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        
pre_save.connect(pre_save_post_receiver, Course)