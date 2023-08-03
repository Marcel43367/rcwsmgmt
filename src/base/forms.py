from django.forms import Form, Textarea, CharField, BooleanField

class WorkshopFeedbackForm(Form):
	subject = CharField(required=True, max_length=256)
	message = CharField(widget=Textarea, required=True)

class WorkshopAnnotateForm(Form):
	annotate = BooleanField(required=True, label='Alle Workshops mit Status "Okay" durchnummerieren')

class WorkshopPrintForm(Form):
	generate_batch = BooleanField(required=True, label="Einen neuen Druckauftrag für alle ungedruckten Workshops erstellen")
