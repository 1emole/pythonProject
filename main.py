class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'advertisements'

        class Advertisement(models.Model):
            title = models.CharField(max_length=255)
            price = models.DecimalField(max_digits=5, decimal_places=2)

            def __str__(self):
                return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"