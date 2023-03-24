from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from django.utils.translation import gettext_lazy as _
from .models import *
from drf_writable_nested import WritableNestedModelSerializer

### PAGINATION ###
class Paginacion(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 6
    

### API MODELS ####
class storeSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
        model = Store
        fields = ('id', 'name', 'location','sales_tax','language','created_at','updated_at')
        read_only_fields = ('id',)
class imageSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
        model = Image
        fields = ('id', 'image_url','created_at','updated_at', 'type')
        read_only_fields = ('id',)

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','tag','class_css')
        read_only_fields = ('id',)

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category')
        read_only_fields = ('id',)
        pagination_class = Paginacion

class ProCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id','category')
        read_only_fields = ('id',)
        pagination_class = Paginacion

class blogimageSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
        model = Image
        fields = ('id', 'image_url','created_at','updated_at')
        read_only_fields = ('id',)

class recipeimageSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
        model = Recipeimage
        fields = ('id', 'image_url','created_at','updated_at')
        read_only_fields = ('id',)

class productSerializer(serializers.ModelSerializer):
    product_images = imageSerializer(many=True)
    category =ProCategorySerializer(many=True)
    """ Seriliazer for the lead object """
    class Meta:
        model = Product
        fields = ('id', 'quantity', 'description','store','price','created_at','updated_at', 'precio_comparacion',
                  'is_destacado', 'is_masvendido', 'name', 'product_images', 'category', 'short_description')
        read_only_fields = ('id',)
class sliderSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
        model = Slider
        fields = ('id', 'data', 'is_active','created_at','updated_at')
        read_only_fields = ('id',)

class blogSerializer(serializers.ModelSerializer):
    blog_images = blogimageSerializer(many=True)
    blog_tags = tagSerializer(many=True)
    blog_category = categorySerializer(many=True)
    """ Seriliazer for the lead object """
    class Meta:
        model = Blog
        fields = ('id', 'blog_title', 'author','reading_time','blog_images','created_at','updated_at', 'blog_content',
                  'slug', 'publish', 'tags','category')
        read_only_fields = ('id',)
        pagination_class = Paginacion

    
class recipeSerializer(serializers.ModelSerializer):
    recipe_images = recipeimageSerializer(many=True)
    recipe_tags = tagSerializer(many=True, source="tags")
    recipe_categories = categorySerializer(many=True, source="category")
    """ Seriliazer for the lead object """
    class Meta:
        model = Recipe
        fields = ('id', 'recipe_title', 'author','recipe_portions','recipe_images','created_at','updated_at', 'recipe_time',
                  'recipe_ingredients','recipe_preparation','slug', 'publish', 'recipe_tags','recipe_categories', 'summary')
        read_only_fields = ('id',)


class contactformSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
            model = Contactform
            fields = '__all__'
            read_only_fields = ('id',)
class lineitemSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    product = productSerializer()
    class Meta:
            model = Lineitem
            fields = '__all__'
            read_only_fields = ('id',)
class orderSerializer(serializers.ModelSerializer):
    """ Seriliazer for the orders"""
    products = lineitemSerializer(many=True)
    class Meta:
            model = Order
            fields = '__all__'
            read_only_fields = ('id',)



class shippingSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
            model = Shipping
            fields = '__all__'
            read_only_fields = ('id',)

class addressSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
            model = Address
            fields = '__all__'
            read_only_fields = ('id',)

class puntosVentasSerializer(serializers.ModelSerializer):
    """ Seriliazer for the lead object """
    class Meta:
            model = puntosVentas
            fields = '__all__'
            read_only_fields = ('id',)





    