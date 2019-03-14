from django.core.exceptions import ValidationError


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ppt', '.pptx', '.pps']# .ppt, .pptx, .pps
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'only ppt, pptx, pps extensions are allowed')