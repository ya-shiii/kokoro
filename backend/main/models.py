from django.db import models
from core.models import User
from django.utils.text import slugify, get_valid_filename
import unicodedata
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import os

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sales_tax = models.FloatField()
    curreny = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mailchimp_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    short_description = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_destacado = models.BooleanField(default = False)
    is_masvendido = models.BooleanField(default = False)
    precio_comparacion = models.FloatField()
    tradegecko_id = models.IntegerField()
    mailchimp_id = models.CharField(max_length=255, blank=True, null=True)
    odoo_id = models.CharField(max_length=200, blank=True, null=True) 
    category = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return self.name

def cleanName(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def imageName(instance, filename):
    filebase, extension = filename.split('.')   
    if instance.type == 'product':
        if instance.id == None:
            ultimaimg = Image.objects.latest('id')
            id_str = str(ultimaimg.id + 1)
        else:
            id_str = str(instance.id)
        filename = get_valid_filename(instance.type+'_'+id_str+instance.product.name+'.'+extension).lower()
    else:
        filename = get_valid_filename(instance.type+'_'+instance.product.name+'.'+extension).lower()
    filename = cleanName(filename)
    return "product_image/"+str(filename)

class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images",
                             related_query_name="product_image",)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    image_file = models.ImageField(upload_to=imageName,default='null')
    type = models.CharField(max_length=150, null=True, choices=[('front', 'front'), ('product', 'product'), ('front_short', 'front_short'),
                                                            ('main', 'main'), ('front_mobile', 'front_mobile')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)+": "+ str(self.type)+" - "+ str(self.product.name) + " "
    
    def save(self, *args, **kwargs):
        tamanoNombre = len(self.image_file.name.split('.'))
        if tamanoNombre >2:
            filebase, extension = self.image_file.name.split('.')[0] , self.image_file.name.split('.')[tamanoNombre-1]
        else:
            filebase, extension = self.image_file.name.split('.')
        if self.image_url is None:
            self.image_url = "https://api.kokorofoods.cl/media/"
        if self.image_file.name.split('/')[len(self.image_file.name.split('/'))-1] != self.image_url.split('/')[len(self.image_url.split('/'))-1]:
            self.image_file.name = get_valid_filename(self.type+'_'+self.product.name+'.'+extension).lower()
            self.image_file.name = "product_image/"+cleanName(self.image_file.name)
            self.image_url = "https://api.kokorofoods.cl/media/"+self.image_file.name
        super(Image, self).save(*args, **kwargs)

# @receiver(pre_save, sender=Image)
# def file_update(sender, **kwargs):
#     print(kwargs['instance'].image_file, '235234542235')
#     upload_folder_instance = kwargs['instance']
#     if upload_folder_instance.image_file:
#         path = upload_folder_instance.image_file.path
#         print("/home/pi/Desktop/kokorofoods/kokorofoods2.0"+path)
#         try:
#             os.remove(path)
#             print('elimino', path,kwargs['instance'].image_file.name,kwargs['instance'].image_file.url)
#         except:
#             print('noup', path,kwargs['instance'].image_file.name,kwargs['instance'].image_file.url)
#             pass


@receiver(post_save, sender=Image)
def url_change(sender,instance, created, **kwargs):
    imagen = instance.image_file
    print('chand',imagen.name.split('/')[len(imagen.name.split('/'))-1],instance.image_url.split('/')[len(instance.image_url.split('/'))-1])
    if imagen.name.split('/')[len(imagen.name.split('/'))-1] != instance.image_url.split('/')[len(instance.image_url.split('/'))-1]:
        print('entro')
        instance.image_url = "https://api.kokorofoods.cl/media/"+imagen.name
        print(instance.image_url)
        instance.save()


class Slider(models.Model):
    data = models.JSONField()
    is_active = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    class_css = models.CharField(max_length=255,default='receta')

    def __str__(self):
        return self.tag

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Blog(models.Model):
    blog_title = models.CharField(max_length = 200)
    author = models.CharField(max_length=200)
    reading_time = models.CharField(max_length=200) 
    blog_content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.blog_title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_title)
        super(Blog, self).save(*args, **kwargs)

class Blogimage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_images",
                             related_query_name="blog_image",)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    image_file = models.ImageField(upload_to='blog_image/',default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if "blog_image" in self.image_file.name:
            self.image_url = "https://api.kokorofoods.cl/media/"+self.image_file.name
        else:
            self.image_url = "https://api.kokorofoods.cl/media/blog_image/"+self.image_file.name
        
        super(Blogimage, self).save(*args, **kwargs)

class Recipe(models.Model):
    recipe_title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    recipe_portions = models.CharField(max_length = 200)
    recipe_time = models.CharField(max_length = 200)
    recipe_ingredients = models.TextField()
    recipe_preparation = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    summary = models.CharField(max_length=200, null=True)
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.recipe_title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipe_title)
        super(Recipe, self).save(*args, **kwargs)

class Recipeimage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_images",
                             related_query_name="recipe_image",)
    
    image_file = models.ImageField(upload_to='recipe_image/',default='null')                          
    image_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if "recipe_image" in self.image_file.name:
            self.image_url = "https://api.kokorofoods.cl/media/"+self.image_file.name
        else:
            self.image_url = "https://api.kokorofoods.cl/media/recipe_image/"+self.image_file.name
        super(Recipeimage, self).save(*args, **kwargs)

class Contactform(models.Model):
    motivo = models.CharField(max_length = 200)
    nombre = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 254)
    mensaje = models.CharField(max_length = 20000)

class Shipping(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, blank=True, null=True)
    country = models.CharField(max_length = 200, blank=True, null=True)
    state = models.CharField(max_length = 200, blank=True, null=True)
    city = models.CharField(max_length = 200, blank=True, null=True)
    comuna = models.CharField(max_length = 200, blank=True, null=True)
    street = models.CharField(max_length = 200, blank=True, null=True)
    number = models.CharField(max_length = 200, blank=True, null=True)
    zipcode = models.CharField(max_length = 200, blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)
    is_default = models.BooleanField(default=True)
    tradegecko_id = models.CharField(max_length = 200, blank=True, null=True)
    odoo_id = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(null=True, max_length=50)
    rut = models.CharField(blank=True, null=True, max_length=30)

class Lineitem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField(Lineitem, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    internal_status = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)
    payment_method = models.CharField(max_length=200, blank=True, null=True)
    sales_tax = models.FloatField(blank=True, null=True)
    total_gross = models.FloatField(blank=True, null=True)
    total_net = models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(blank=True, null=True) 
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    last_4_digits = models.CharField(max_length=200, blank=True, null=True)   
    tracking_number = models.CharField(max_length=200, blank=True, null=True)
    carrier = models.CharField(max_length=200, blank=True, null=True) 
    order_number = models.IntegerField(blank=True, null=True)
    payku_transaction_id =  models.CharField(max_length=200, blank=True, null=True)
    payku_verification_key =  models.CharField(max_length=200, blank=True, null=True)
    mailchimp_id = models.CharField(max_length=200, blank=True, null=True)
    odoo_id = models.CharField(max_length=200, blank=True, null=True) 
    lioren_id = models.CharField(max_length=200, blank=True, null=True) 
    tradegecko_id = models.CharField(max_length=200, blank=True, null=True) 
    folio_sii = models.CharField(max_length=200, blank=True, null=True) 
    boleta_pdf = models.CharField(max_length=2000, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return '%s' % (self.order_number)

class Logincodes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=200, blank=True, null=True) 
    expiration_date = models.DateTimeField()


class puntosVentas(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    telefono = models.IntegerField(blank=True, null=True)
    website = models.URLField(max_length=300, blank=True, null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    email = models.EmailField(max_length=254, null=True)
    creado_el = models.DateField(auto_now=True)

    class Meta:
        """Meta definition for puntosVentas."""

        verbose_name = 'punto de venta'
        verbose_name_plural = 'punto de ventas'

    def __str__(self):
         return '%s %s' % (self.nombre, self.creado_el)

class zoho(models.Model):
    access_token = models.CharField(max_length=500)
    refresh_token = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
