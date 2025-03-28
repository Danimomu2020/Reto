from django.db import models

class Vulnerability(models.Model):
    cve_id = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    severity = models.CharField(max_length=10)  # Puedes usar un ChoiceField para valores predefinidos
    fixed = models.BooleanField(default=False)

    def __str__(self):
        return self.cve_id