from django.db import models

from applications.globals.models import ExtraInfo


class File(models.Model):
    ref_id = models.IntegerField(unique=True, null=True, blank=True)
    uploader = models.ForeignKey(
        ExtraInfo, on_delete=models.CASCADE, related_name='uploaded_files')
    subject = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(blank=True)
    complete_flag = models.BooleanField(default=False)

    class Meta:
        db_table = 'File'

    def __str__(self):
        return str(self.ref_id)


class Tracking(models.Model):
    file_id = models.ForeignKey(File, on_delete=models.CASCADE, null=True)
    current_id = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(
        ExtraInfo, on_delete=models.CASCADE, related_name='receiver_id')
    receive_date = models.DateTimeField(auto_now_add=True)
    forward_date = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)
    upload_file = models.FileField(blank=True)

    class Meta:
        db_table = 'Tracking'
