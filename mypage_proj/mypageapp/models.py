from django.db import models
from django.contrib.auth.models import User #Accessing User module from admin portal
from django.utils import timezone
from django.urls import reverse



class UserProfInfoA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Pointing to existing User class in admin pannel. Connecting new attribute to existing user model in admin.
    portfolio_site = models.URLField(blank=True,max_length = 260)
    location = models.CharField(blank=True,max_length = 260)
    ############## added for image############
    document = models.FileField(upload_to='profile_pic/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Create your models here.

class UserProfile(models.Model):
    username = models.ForeignKey('auth.User',on_delete=models.CASCADE )
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    dateofbirth = models.DateField(max_length = 15)
    gender = models.CharField(max_length = 100)
    father_name = models.CharField(max_length = 100)
    mother_name = models.CharField(max_length = 100)
    add_line1 = models.CharField(max_length = 300)
    add_line2 = models.CharField(max_length = 300,blank=True,null=True)
    add_line3 = models.CharField(max_length = 300,blank=True,null=True)
    occupation = models.CharField(max_length = 100)
    adhaar = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 100)
    blood_group = models.CharField(max_length = 100)
    marital_status = models.CharField(max_length = 100)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
         return self.last_name


class UserEduDetails(models.Model):
    username = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    qualification1 = models.CharField(max_length = 100)
    qual1_stream = models.CharField(max_length = 100)
    qual1_sub = models.CharField(max_length = 100)
    qual1_pass_year = models.DateField(max_length = 15)
    qual1_college = models.CharField(max_length = 100)
    qualification2 = models.CharField(max_length = 100)
    qual2_stream = models.CharField(max_length = 100)
    qual2_sub = models.CharField(max_length = 100)
    qual2_pass_year = models.DateField(max_length = 15)
    qual2_college = models.CharField(max_length = 100)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def __str__(self):
         return self.username


class UserSkillDetails(models.Model):
    username = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    skill = models.CharField(max_length = 100)
    work_location = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    work_exp = models.CharField(max_length = 100)
    expertise = models.CharField(max_length = 100)
    created_date = models.DateTimeField(default=timezone.now())
    modified_date = models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("userprofile_detail",kwargs={'pk':self.pk})

    def __str__(self):
         return self.username
