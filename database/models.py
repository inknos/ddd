from django.db import models
from django.utils import timezone

# Create your models here.
class Contributor(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Name of contributor"
    )

    email = models.EmailField(
        max_length=200,
        default="",
        blank=True,
        help_text="Main E-Mail of the contributor"
    )

    institution = models.ForeignKey(
        'Institution',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="Institution where the contributor belongs to",
    )

    date_of_addition = models.DateTimeField(
        auto_now_add=True, editable=False
    )
    modification_date = models.DateTimeField(
        auto_now=True, editable=False
    )

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Institution name"
    )

    date_of_addition = models.DateTimeField(
        auto_now_add=True, editable=False
    )

    modification_date = models.DateTimeField(
        auto_now=True, editable=False
    )

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Action name",
    )

    date_of_addition = models.DateTimeField(
        auto_now_add=True, editable=False
    )

    modification_date = models.DateTimeField(
        auto_now=True, editable=False
    )
    def __str__(self):
        return self.name

class Contribution(models.Model):
    name_of_contributor = models.ForeignKey(
        'Contributor',
        on_delete=models.CASCADE,
    )

    action_type = models.ForeignKey(
        'Action',
        on_delete=models.CASCADE,
    )

    target_institution = models.ForeignKey(
        'Institution',
        on_delete=models.CASCADE,
    )

    date_of_contribution = models.DateField(default=timezone.now)
    date_of_addition = models.DateTimeField(
        auto_now_add=True, editable=False
    )
    modification_date = models.DateTimeField(
        auto_now=True, editable=False
    )
    def __str__(self):
        return self.date_of_contribution.strftime('%m/%d/%Y') + ": " + self.name_of_contributor.name + ": " + self.action_type.name + " " + self.target_institution.name

