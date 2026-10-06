from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_runtimesetting"),
    ]

    operations = [
        migrations.CreateModel(
            name="Participant",
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
                (
                    "participant_id",
                    models.CharField(
                        max_length=64,
                        unique=True,
                        verbose_name="Teilnehmer-ID",
                    ),
                ),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participants",
                        to="base.order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="participant",
            name="votes",
            field=models.ManyToManyField(
                blank=True,
                related_name="voted_participants",
                to="base.workshop",
            ),
        ),
    ]