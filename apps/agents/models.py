from djongo import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()

class Agent(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    
    class Meta:
        db_table = 'agents'
    
    def __str__(self):
        return f"Agent: {self.user.name}"

class VerifiedSupplier(BaseModel):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('pending', 'Pending'),
    ]
    
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='verified_suppliers')
    supplier_id = models.CharField(max_length=100)  # Reference to supplier
    verification_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    class Meta:
        db_table = 'verified_suppliers'
    
    def __str__(self):
        return f"Agent {self.agent.user.name} - Supplier {self.supplier_id} - {self.status}"