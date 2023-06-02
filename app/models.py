from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ZIM = (
    ("Alaqa Zimmedar Naik Aamal","Alaqa Zimmedar Naik Aamal"),
    ("District Zimmedar Naik Aamal","District Zimmedar Naik Aamal"),
    ("Division Zimmedar Naik Aamal","Division Zimmedar Naik Aamal"),
    ("State Zimmedar Naik Aamal","State Zimmedar Naik Aamal"),
    ("Region Zimmedar Naik Aamal","Region Zimmedar Naik Aamal"),
    ("Hind Zimmedar Naik Aamal","Hind Zimmedar Naik Aamal"),
    ("Other Zimmedar","Other Zimmedar"),
)


class Region(models.Model):
    region_name = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return str(self.region_name)


class State(models.Model):
    region_namef = models.ForeignKey(Region, on_delete=models.CASCADE,default='',null=True)
    state_name = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return str(self.state_name)


class Division(models.Model):
    state_namef = models.ForeignKey(State, on_delete=models.CASCADE,default='',null=True)
    division_name = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return str(self.division_name)

class District(models.Model):
    division_namef = models.ForeignKey(Division, on_delete=models.CASCADE,default='',null=True)
    district_name = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return str(self.district_name)


class Zimmedar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default='',null=True)
    zehliHalqa = models.CharField(max_length=200,default='',null=True) 
    alaqa = models.CharField(max_length=200,default='',null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,default='',null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE,default='',null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,default='',null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,default='',null=True)

    def __str__(self):
        return str(self.id)

class Report(models.Model):
    zimmedar = models.ForeignKey(User, on_delete=models.CASCADE,default='',null=True)
    zimmedar_name = models.CharField(max_length=100,default='',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    zimmedari = models.CharField(choices=ZIM,default='madinah',max_length=50,null=True)
    alaqa = models.CharField(max_length=100,default='',null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,default='',null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE,default='',null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,default='',null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,default='',null=True)
    taqseem = models.BigIntegerField(default=0,null=True)
    wusool = models.BigIntegerField(default=0,null=True)
    islaheaamal_ijtima_maqam = models.BigIntegerField(default=0,null=True)
    islaheaamal_ijtima_shuraqa = models.BigIntegerField(default=0,null=True)
    tahajjud_ijtima_maqam = models.BigIntegerField(default=0,null=True)
    tahajjud_ijtima_shuraqa = models.BigIntegerField(default=0,null=True)
    sehri_ijtima_maqam = models.BigIntegerField(default=0,null=True)
    sehri_ijtima_shuraqa = models.BigIntegerField(default=0,null=True)
    mehboob_e_attar = models.BigIntegerField(default=0,null=True)
    yaumequfle_madinah_maqam = models.BigIntegerField(default=0,null=True)
    yaumequfle_madinah_shuraqa = models.BigIntegerField(default=0,null=True)
    haftawar_ijtima_main_raat_guzarne_wale_Shuraqa = models.BigIntegerField(default=0,null=True)
    haftawar_ijtima_main_raat_guzarne_wale_maqam = models.BigIntegerField(default=0,null=True)

    
    def __str__(self):
        return str(self.id)