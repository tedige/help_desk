from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Problem(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('resolved', 'Решена'),
        ('confirmed', 'Подтверждена')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_user = models.ForeignKey(User, related_name='assigned_problems', null=True, blank=True, on_delete=models.SET_NULL)
    resolved_user = models.ForeignKey(User, related_name='resolved_problems', null=True, blank=True, on_delete=models.SET_NULL)
    reception_group, created = Group.objects.get_or_create(name='Reception')
    tester_group, created = Group.objects.get_or_create(name='Tester')

    def __str__(self):
        return self.name


