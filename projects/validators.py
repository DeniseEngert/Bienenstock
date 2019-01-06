from django.core.exceptions import ValidationError
import os
import csv

def validate_csv(value):
    # check if extension is correct
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

    # try to parse csv file
    try:
        str_text = ''
        for line in value.file:
            str_text = str_text + line.decode()
        csv.reader(value.file)
    except:
        raise ValidationError(u'Wrong format.')

