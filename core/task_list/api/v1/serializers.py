from rest_framework import serializers
from ...models import Task


class taskSerializer(serializers.ModelSerializer):

    relative_path = serializers.URLField(source = 'get_relative_api_url',read_only = True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields =['id','user','title','complete','created_date','updated_date','absolute_url','relative_path']
        read_only_fields = ['user']
    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self,instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('relative_path')
            rep.pop('absolute_url')
            return rep
        return rep


    def create(self,validate_data):
        validate_data['user'] = self.context.get('request').user
        return super().create(validate_data)