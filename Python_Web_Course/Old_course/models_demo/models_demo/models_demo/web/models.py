from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Id: {self.pk}; Name: {self.name}"

class Project(models.Model):
    name = models.CharField(max_length=20)
    code_name = models.CharField(max_length=20)
    deadline = models.DateField()

    def __str__(self):
        return f"Id: {self.pk}; Name: {self.name}; Code name: {self.code_name}; Deadline: {self.deadline}"


class Employee(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_MIDDLE = 'Middle'
    LEVEL_SENIOR = 'Senior'
    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_MIDDLE, LEVEL_MIDDLE),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(max_length=40)

    last_name = models.CharField(
        max_length=40,
        null=True,
    )
    level = models.CharField(
        max_length=25,
        choices=LEVEL_CHOICES,
        verbose_name='Seniority level'
    )

    years_of_experience = models.PositiveSmallIntegerField()

    start_date = models.DateField()

    email = models.EmailField(
        unique=True,
        editable=False,
    )

    review = models.TextField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    photo = models.URLField(
        blank=True,
    )

    will_receive_bonus = models.BooleanField(
        default=False,
        # null=True,
        # testing null=True on Boolean
    )
    department=models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    project = models.ManyToManyField(Project)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.full_name}'

class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Category(models.Model):
    name = models.CharField(max_length=20)

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True,
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )