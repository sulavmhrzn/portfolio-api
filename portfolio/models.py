from django.db import models


class Skill(models.Model):
    class LevelChoice(models.TextChoices):
        BEGINNER = "Beginner"
        INTERMEDIATE = "Intermediate"
        ADVANCED = "ADVANCED"

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LevelChoice.choices)
    years_of_exp = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    network = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self) -> str:
        return self.network


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.CharField(help_text="comma separated value", max_length=200)
    summary = models.TextField()
    repo_url = models.URLField(blank=True, default="")
    live_url = models.URLField(blank=True, default="")
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=200)
    area = models.CharField(help_text="Computer", max_length=100)
    description = models.TextField()
    study_type = models.CharField(
        help_text="Bachelors in computer applications", max_length=100
    )
    score = models.DecimalField(max_digits=4, decimal_places=2)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.institution


class Certificate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False, blank=True, null=True)
    summary = models.TextField()

    def __str__(self) -> str:
        return self.name


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    label = models.TextField(max_length=200)
    image = models.ImageField(upload_to="profile")
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=10, blank=True, default="")
    summary = models.TextField()
    blog = models.URLField(blank=True, default="")

    skill = models.ManyToManyField(Skill)
    profile = models.ManyToManyField(Profile)
    education = models.ManyToManyField(Education)
    work = models.ManyToManyField(Work)
    project = models.ManyToManyField(Project)
    certificate = models.ManyToManyField(Certificate)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About me"
