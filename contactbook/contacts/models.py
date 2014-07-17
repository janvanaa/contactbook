from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Contact(models.Model):
    slug       = models.SlugField(max_length=255, editable=False)
    address    = models.CharField(max_length=255, blank=True)
    postcode   = models.CharField(max_length=6, blank=True)
    city       = models.CharField(max_length=255, blank=True)
    phone      = models.CharField(max_length=10, blank=True)
    email      = models.EmailField(blank=True)
    website    = models.URLField(max_length=255, blank=True)
    bank       = models.CharField(max_length=255, blank=True)
    
class Company(Contact):
    name       = models.CharField(max_length=255, unique=True)
    kvk        = models.CharField(max_length=255, blank=True)
    btw        = models.CharField(max_length=255, blank=True)
    branche    = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'companies'
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('company', kwargs = {'pk':self.id})
    
    def get_fields(self):
        f = []
        for field in Company._meta.fields:
            if field.name not in ('id','slug','contact_ptr'):
                f.append((field.name, field.value_to_string(self)))
        f.insert(0, f.pop(7))
        return f
    
    def save(self):
        self.slug = slugify(self.name)
        super(Company, self).save()
            
class Person(Contact):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    works_for  = models.ForeignKey(Company, related_name='employee', blank=True, null=True)
    function   = models.CharField(max_length=255, blank=True)
        
    class Meta:
        unique_together=(('first_name', 'last_name'),)
        
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_absolute_url(self):
        return reverse('person', kwargs = {'pk':self.id})
    
    def get_fields(self):
        f = []
        for field in Person._meta.fields:
            if field.name not in ('id','slug','contact_ptr'):                
                f.append((field.name, field.value_to_string(self)))
        f.insert(0, f.pop(7))
        f.insert(1, f.pop(8))
        f[9] = (f[9][0], Company.objects.get(pk=f[9][1]))
        return f
    
    def save(self):
        slug = self.first_name + ' ' + self.last_name
        self.slug = slugify(slug)
        super(Person, self).save()    

  