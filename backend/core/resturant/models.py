from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
            description = models.TextField(blank=True)
                phone = models.CharField(max_length=20, blank=True)
                    email = models.EmailField(blank=True)
                        opening_time = models.TimeField()
                            closing_time = models.TimeField()
                                created_at = models.DateTimeField(auto_now_add=True)

                                    def __str__(self):
                                            return self.name


                                            class MenuItem(models.Model):
                                                CATEGORY_CHOICES = [
                                                        ('starter', 'Starter'),
                                                                ('main', 'Main Course'),
                                                                        ('dessert', 'Dessert'),
                                                                                ('drink', 'Drink'),
                                                                                    ]

                                                                                        restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
                                                                                            name = models.CharField(max_length=255)
                                                                                                category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
                                                                                                    price = models.DecimalField(max_digits=8, decimal_places=2)
                                                                                                        is_available = models.BooleanField(default=True)
                                                                                                            image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
                                                                                                                description = models.TextField(blank=True)
                                                                                                                    created_at = models.DateTimeField(auto_now_add=True)

                                                                                                                        def __str__(self):
                                                                                                                                return self.name
# Create your models here.
