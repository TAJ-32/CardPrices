from django.contrib import admin
from .models import Card

# create a class for the admin-model integration
class CardPricesAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("name","condition","year")

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Card,CardPricesAdmin)