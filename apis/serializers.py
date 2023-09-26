from rest_framework import serializers
from .models import *

class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ColaboradorModel
		fields = ('id', 'nome', 'score', 'senha', 'id_chefe')
