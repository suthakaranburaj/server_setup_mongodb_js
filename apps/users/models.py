from djongo import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.common.models import BaseModel

class UserManager(BaseUserManager):
    def create_user(self, phone, pin, **extra_fields):
        if not phone:
            raise ValueError('Phone number is required')
        if not pin:
            raise ValueError('PIN is required')
        
        user = self.model(phone=phone, **extra_fields)
        user.set_password(pin)  # This will hash the PIN
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, pin, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        
        return self.create_user(phone, pin, **extra_fields)

class User(AbstractBaseUser, BaseModel):
    ROLE_CHOICES = [
        ('vendor', 'Vendor'),
        ('normal_user', 'Normal User'),
        ('supplier', 'Supplier'),
        ('agent', 'Agent'),
        ('admin', 'Admin'),
    ]
    
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    refresh_token = models.TextField(blank=True, null=True)
    token_version = models.IntegerField(default=0)
    image = models.URLField(blank=True, null=True)
    
    # Django required fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'role']
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return f"{self.name} ({self.phone})"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser