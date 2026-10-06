from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		('base', '0007_participant'),
	]

	operations = [
		migrations.AddField(
			model_name='workshop',
			name='ticket_code',
			field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='Ticketcode'),
		),
	]