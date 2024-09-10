from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):  # (1)
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
