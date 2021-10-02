from rest_framework import serializers
from .models import Project, Skill, Education, Certificate, Profile, AboutMe, Work


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ["id"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ["id"]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ["id"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        exclude = ["id"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["id"]


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        exclude = ["id"]


class AboutMeSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True)
    skill = SkillSerializer(many=True)
    education = EducationSerializer(many=True)
    certificate = CertificateSerializer(many=True)
    profile = ProfileSerializer(many=True)
    work = WorkSerializer(many=True)

    class Meta:
        model = AboutMe
        fields = [
            "name",
            "label",
            "image",
            "email",
            "phone",
            "summary",
            "blog",
            "education",
            "skill",
            "project",
            "work",
            "certificate",
            "profile",
        ]
