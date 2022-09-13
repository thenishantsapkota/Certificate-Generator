# Generated by Django 4.1.1 on 2022-09-13 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields
import web_app.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("avatar", models.ImageField(blank=True, upload_to="profile/")),
                ("username", models.CharField(max_length=100, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("institute_name", models.CharField(blank=True, max_length=100)),
                ("institute_logo", models.ImageField(blank=True, upload_to="logos/")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", web_app.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school_name", models.CharField(max_length=200)),
                ("school_address", models.CharField(max_length=200)),
                ("established_date", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=200
                    ),
                ),
                ("student_name", models.CharField(max_length=200)),
                ("student_fathers_name", models.CharField(max_length=200)),
                ("student_address", models.CharField(max_length=200)),
                ("academic_year", models.CharField(max_length=200)),
                ("program", models.CharField(max_length=200)),
                ("passed_year", models.CharField(max_length=200)),
                ("secured_gpa", models.CharField(max_length=200)),
                ("date_of_birth", models.DateField()),
                ("symbol_number", models.CharField(max_length=200)),
                ("registration_number", models.CharField(max_length=200, unique=True)),
                (
                    "issued_date",
                    models.CharField(default="2079-05-28", max_length=200, null=True),
                ),
                (
                    "certificate",
                    versatileimagefield.fields.VersatileImageField(
                        null=True, upload_to="media/"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
