"""
GAVIP Example AVIS: Simple AVI

Django models used by the AVI pipeline
@req: REQ-0006
@comp: AVI Web System
"""

import datetime
from django.db import models
from pipeline.models import AviJob, AviJobRequest


class DemoModel(AviJob):
    """
    This model is used to store the parameters for the AVI pipeline.
    Notice that it contains identical field names here as is the variables in
    the pipeline itself.

    An AviJob model must contain all fields required by the intended
    pipeline class (ProcessData) in this case.
    """

    # We can override the default time_to_completion function here
    # This is an integer value for the time, in seconds, the job
    # is expected to take
    def time_to_completion(self, avi_model_name, *args, **kwargs):
        jobs = AviJobRequest.objects.filter(avi_model_name=avi_model_name).filter(pipeline_state__progress=100)
        if jobs:
            time_tot = datetime.timedelta(0)
            for job in jobs:
                time_tot = time_tot + job.pipeline_state.last_activity_time - job.created
            mean_time = time_tot.total_seconds()/float(len(jobs))
        else:
            mean_time = 0
        return mean_time

    query = models.CharField(max_length=1000)
    outputFile = models.CharField(default="", max_length=100)
    pipeline_task = "ProcessData"

    def get_absolute_url(self):
        return "%i/" % self.pk
