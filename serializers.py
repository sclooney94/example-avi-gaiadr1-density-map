from rest_framework import serializers
from avi.models import DemoModel


class DemoModelSerializer(serializers.ModelSerializer):
    """Serializer for the attributes of DemoModel as an AviJob, with
    AviJobRequest and PipeState included.
    """
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    expected_runtime = serializers.IntegerField(read_only=True)

    class Meta:
        model = DemoModel
        fields = '__all__'
        depth = 2


class ViewJobsSerializer(serializers.ModelSerializer):
    """Serializer for the 'View Job' page"""

    job_id = serializers.IntegerField(source='request.job_id')
    started = serializers.DateTimeField(source='request.created')
    completed = serializers.DateTimeField(source='request.pipeline_state.last_activity_time')
    progress = serializers.IntegerField(source='request.pipeline_state.progress')
    state = serializers.CharField(source='request.pipeline_state.state')
    result_path = serializers.CharField(source='request.result_path')
    public_result_path = serializers.CharField(source='request.public_result_path')
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = DemoModel
        fields = ('job_id',
                  'started',
                  'completed',
                  'progress',
                  'state',
                  'result_path',
                  'public_result_path',
                  'url')
