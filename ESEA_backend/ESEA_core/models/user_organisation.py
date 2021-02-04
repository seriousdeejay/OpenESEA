from django.db import models

class UserOrganisation(models.Model):
    user = models.ForeignKey('CustomUser', related_name="users", on_delete=models.CASCADE)
    organisation = models.ForeignKey('Organisation', related_name="organisations", on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'organisation']] 