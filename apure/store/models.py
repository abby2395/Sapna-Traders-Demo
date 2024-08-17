from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


# Category table
class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_('Category Name'),
        help_text=_('Required and Unique'),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_('Category Safe Url'), max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = "children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name

# Product Types
class ProductType(models.Model):
    name = models.CharField(
        verbose_name = _("Product Name"),
        help_text = _("Required"),
        max_length = 255,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")
    
    def __str__(self):
        return self.name

# Product Specification
class Product_Specification(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete = models.RESTRICT)
    name = models.CharField(
        verbose_name = _("Name"),
        help_text = _("Required"),
        max_length= 255,
    )

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

        def __str__(self):
            return 

# Product
class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete = models.RESTRICT)
    category = models.ForeignKey(Category, on_delete = models.RESTRICT)
    title = models.TextField(
        verbose_name = _("title"),
        help_text = _("Required"),
        max_length = 255,
    )
    description = models.TextField(
        verbose_name = _("Description"),
        help_text = _("Not Required"),
        blank = True,
    )
    slug = models.SlugField(max_length = 255)

    # Regular Price
    regular_price = models.DecimalField(
        verbose_name = _("Regular Price"),
        help_text = ("Maximum"),
        error_messages = {
            "name" : {
                "max_length" : _("The price must be above 0."),
            },
        },
        max_digits = 5,
        decimal_places = 2,
    )

    # Discount Price
    discounted_price = models.DecimalField(
        verbose_name = _("Discount Price"),
        help_text = ("Maximum"),
        error_messages = {
            "name" : {
                "max_length" : _("The price must be above 0."),
            },
        },
        max_digits = 5,
        decimal_places = 2,
    )

    # Availibility
    is_active = models.BooleanField(
        verbose_name = _("Product Visibility"),
        help_text = _("Change product visibility"),
        default = True,
    )