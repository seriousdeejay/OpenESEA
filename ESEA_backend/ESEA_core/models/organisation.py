from django.db  import models
from django.utils.translation import gettext_lazy as _
    
class Organisation(models.Model):
    name = models.CharField(max_length=255, unique=False, blank=False)
    description = models.TextField(blank=True)
    # image = models.ImageField(blank=True, upload_to="organisation/", default="organisation/default.png")
    users = models.ManyToManyField('CustomUser', through='UserOrganisation')


    class Meta:
        verbose_name = _('organisation')
        verbose_name_plural = _('organisations')

    def __str__(self):
        return self.name