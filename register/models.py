from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    userName=None
    phone_number=models.CharField(unique=True,max_length=100)
    email=models.EmailField(unique=True)
    otp=models.CharField(max_length=6,null=True,blank=True)
    user_profile_image=models.ImageField(upload_to="images")
    is_verified=models.BooleanField(default=False)
    
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=True)

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
    def has_perm(self, perm, obj=None):
        """
        Does the user have a specific permission?
        """
        return True  # You can customize this logic as needed

    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        """
        return True  # You can customize this logic as needed
