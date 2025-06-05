from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length = 60, default = "", blank = True, null = False)
    State = models.CharField(max_length = 2, default = "", blank = True, null = False)
    Campus_ID = models.IntegerField(default = "", blank = True, null = False)

    objects = models.Manager()

    def __str__(self):
        # Returns the input value of the Campus and State name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.Campus_name} - {0.State}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name = 'University Campus'