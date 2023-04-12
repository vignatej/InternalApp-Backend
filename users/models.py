from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name=models.CharField(null=False, max_length=30)
    email=models.EmailField(null=False)
    Branches=[('cse',"cse"),('ece','ece'),('eee','eee'),('chem','chem')]
    branch=models.CharField(choices=Branches, null=False, max_length=5)
    years=[(2019,2019),(2020,2020),(2021,2021),(2022,2022),(2023,2023),(2024,2024),(2025,2025),(2026,2026),(2027,2027)]
    startYear=models.IntegerField(choices=years, null=False)
    tagline=models.CharField(max_length=25, null=True)
    profilePhoto=models.ImageField(null=False, default='default.png')

    @property
    def endyear(self):
        return str(int(self.startYear)+4)
    
    def __str__(self) -> str:
        return self.name