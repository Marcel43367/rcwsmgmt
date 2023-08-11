from django.forms import Form, Textarea, CharField, BooleanField, ModelChoiceField
from base.models import WorkshopList

class WorkshopFeedbackForm(Form):
	subject = CharField(required=True, max_length=256)
	message = CharField(widget=Textarea, required=True)

class WorkshopAnnotateForm(Form):
	annotate = BooleanField(required=True, label='Alle Workshops mit Status "Okay" durchnummerieren')

class WorkshopPrintForm(Form):
	generate_batch = BooleanField(required=True, label="Einen neuen Druckauftrag für alle ungedruckten Workshops erstellen")

class WorkshopAddToListForm(Form):
	workshop_list = ModelChoiceField(WorkshopList.objects.all(), label="Workshopliste")

class WorkshopRemoveFromListForm(Form):
	pass