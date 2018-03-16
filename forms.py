from wtforms import Form, TextField, HiddenField

class LandingForm(Form):
    f1 = StringField("uname")
    f2 = DecimalField("pp")

class NextForm(Form):
    f1 = StringField("hiddenuname")
    f2 = DecimalField("pp")
