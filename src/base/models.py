from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, PositiveIntegerField, DateTimeField, ForeignKey, CASCADE
from django.db.models import BooleanField, SET_NULL, Sum
class Order(Model):
	clan = CharField(
		max_length=64,
		verbose_name="Stamm",
	)
	district = CharField(
		max_length=128,
		verbose_name="Diözese / Bezirk",
	)
	first_name = CharField(max_length=64, verbose_name="Vorname")
	last_name = CharField(max_length=64, verbose_name="Nachname")
	participant_count = PositiveIntegerField()
	code = CharField(
		max_length=16,
		verbose_name="Bestellungscode",
		db_index=True
	)

	def get_pretix_url(self):
		return f"{settings.PRETIX_URL}control/event/{settings.PRETIX_ORGANIZER}/{settings.PRETIX_EVENT}/orders/{self.code}/"

	def sufficient_workshops(self):
		order_weq = self.workshop_set.all().aggregate(Sum("weq"))['weq__sum']
		return max(1, int(self.participant_count / settings.WORKSHOPS_PER_PARTICIPANT)) <= order_weq


class WorkshopPrintBatch(Model):
	created = DateTimeField(auto_now_add=True)

class Workshop(Model):
	STATUS_NEW = "A"
	STATUS_REVISED = "E"
	STATUS_REJECTED = "R"
	STATUS_UNCLEAR = "U"
	STATUS_OKAY = "V"
	STATUS_CHOICE=(
		(STATUS_NEW, "Neuer Workshop"),
		(STATUS_REVISED, "Workshop überarbeitet"),
		(STATUS_OKAY, "Workshop okay"),
		(STATUS_REJECTED, "Workshop nicht okay"),
		(STATUS_UNCLEAR, "Workshop unklar"),
	)
	name = CharField(max_length=64, verbose_name="Name")
	order = ForeignKey(Order, on_delete=CASCADE)
	description = TextField(verbose_name="Beschreibung")
	position_id = PositiveIntegerField()
	weq = PositiveIntegerField(default=1, verbose_name="Workshop Äquivalenz Punkte")
	status = CharField(max_length=1, choices=STATUS_CHOICE, verbose_name="Status")
	printed = ForeignKey(WorkshopPrintBatch, null=True, on_delete=SET_NULL)
	annotated_id = PositiveIntegerField(null=True)


class LogEntry(Model):
	workshop = ForeignKey(Workshop, on_delete=CASCADE)
	by_customer = BooleanField(default=False)
	user = ForeignKey(User, null=True, on_delete=SET_NULL, related_name="rcwsmgmt_logentries")
	created = DateTimeField(auto_now_add=True)
	old_status = CharField(max_length=1, null=True, choices=Workshop.STATUS_CHOICE, verbose_name="Alter Status")
	new_status = CharField(max_length=1, choices=Workshop.STATUS_CHOICE, verbose_name="Neuer Status")
	action = CharField(max_length=64)
	title = CharField(max_length=64, verbose_name="Betreff")
	message = TextField(verbose_name="Nachricht")
