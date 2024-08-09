from utils.serializers.base_serializer import BaseSerializer
import cloudpickle, pickle


class CloudPickleUtil(BaseSerializer):
    def serialize(self, obj):
        return cloudpickle.dumps(obj)

    def deserialize(self, data):
        return pickle.loads(data)
