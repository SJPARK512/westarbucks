from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'


class Category(models.Model):
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'


class Products(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    nutrition_id = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'


class Allergy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergy'


class AllergyProducts(models.Model):
    allergy_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    products_id = models.ForeignKey('Products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    products_id = models.ForeignKey('Products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'nutritions'
