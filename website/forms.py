from flask import Flask, request
from flask_wtf import Form
from wtforms import SelectMultipleField, SubmitField


class Select2MultipleField(SelectMultipleField):

    def pre_validate(self, form):
        # Prevent "not a valid choice" error
        pass

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = ",".join(valuelist)
        else:
            self.data = ""

class Form(Form):
    multi_select = Select2MultipleField("Ingredients", [],
            choices=[("py", "python"), ("rb", "ruby"), ("js", "javascript")],
            description="Ingredients",
            render_kw={"multiple": "multiple"})
    submit = SubmitField()