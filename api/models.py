from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

# Create your models here.


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deleted = models.BooleanField(default=False)

    
class PriceList(BaseModel):
    class PriceListChoices(models.IntegerChoices):
        SELLING = 1, "selling"
        BUYING = 2, "buying"

    price_list = models.IntegerField(choices=PriceListChoices.choices, null=False, blank=False)
    price_list_rate = models.FloatField()

    def __str__(self) -> str:
        return self.get_price_list_display() + " : " + str(self.price_list_rate)


class Item(BaseModel):
    item_name = models.CharField(max_length=255, blank=False, null=False)
    item_code = models.CharField(max_length=255, blank=False, null=False)
    price_list = models.ManyToManyField(PriceList)

    def __str__(self) -> str:
        return self.item_name
