from django.db import models
from django.db.models.fields.files import ImageField
from PIL import Image
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
# class ProjectDetails(models.Model):
#     fy = models.CharField(max_length=255, blank=True, null=True)
#     project_status = models.CharField(max_length=255, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     implementing_agency = models.CharField(max_length=255, blank=True, null=True)
#     tot_project_outlay = models.CharField(max_length=255, blank=True, null=True)
#     lat = models.CharField(max_length=255, blank=True, null=True)
#     lng = models.CharField(max_length=255, blank=True, null=True)
#     id = models.IntegerField(primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'project_details'
class CoalForm(models.Model):
    project_name=models.CharField(max_length = 250, default='', blank=True,null = True)
    inputState=models.CharField(max_length = 250, default='', blank=True,null = True)
    inputDistrict=models.CharField(max_length = 250, default='', blank=True,null = True)
    fy=models.CharField(max_length = 250, default='', blank=True,null = True)
    Projectstatus=models.CharField(max_length = 250, default='', blank=True,null = True)
    agencytype=models.CharField(max_length = 250, default='', blank=True,null = True)
    organisation_name=models.CharField(max_length = 250, default='', blank=True,null = True)
    tender_receipt=models.DateField(blank=True, null=True)
    sector=models.CharField(max_length = 250, default='', blank=True,null = True)
    request_amount=models.IntegerField(blank=True, null=True)
    approved_amount=models.IntegerField(blank=True, null=True)
    security_completion=models.DateField(blank=True, null=True)
    submission=models.DateField(blank=True, null=True)
    receipt=models.DateField(blank=True, null=True)
    agenda_completion=models.DateField(blank=True, null=True)
    committee_review=models.DateField(blank=True, null=True)
    # gm_csr_sign_off=models.DateField(blank=True, null=True)
    vetting_by_dp=models.DateField(blank=True, null=True)
    vetting_by_df=models.DateField(blank=True, null=True)
    chairman_approval=models.DateField(blank=True, null=True)
    csr_sd_committee_review=models.DateField(blank=True, null=True)
    cil_board_review=models.DateField(blank=True, null=True)
    fcbc_completion=models.DateField(blank=True, null=True)
    mou_finalisation=models.DateField(blank=True, null=True)
    gm_csr_sign_off=models.DateField(blank=True, null=True)
    legal_security=models.DateField(blank=True, null=True)
    office_orfder_creation=models.DateField(blank=True, null=True)
    finance=models.DateField(blank=True, null=True)
    fund_disbursal=models.DateField(blank=True, null=True)
    first_release_ack=models.DateField(blank=True, null=True)
    final_release_ack=models.DateField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='CoalIndiaPics/', blank=True, null=True, default='CoalIndiaPics/noImage.jpg')
    files = models.FileField(upload_to='CoalIndiaFiles/', blank=True, null=True)
    commpendium = models.FileField(upload_to='CoalIndiaCompendiums/', blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(CoalForm, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture
    def __str__(self):
        return self.project_name