from django.db import models

# Create your models here.
class ProjectDetails(models.Model):
    fy = models.CharField(max_length=255, blank=True, null=True)
    project_status = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    implementing_agency = models.CharField(max_length=255, blank=True, null=True)
    tot_project_outlay = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'project_details'