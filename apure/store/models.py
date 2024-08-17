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

