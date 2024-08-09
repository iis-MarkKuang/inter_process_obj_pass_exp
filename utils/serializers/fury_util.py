from collections import deque
from threading import Condition

from serializable_collections.serializablequeue import SerializableQueue
from test_class.simple_class import SimpleClass
from utils.serializers.base_serializer import BaseSerializer
import pyfury


class FuryUtil(BaseSerializer):
    def __init__(self):
        self.fury_inst = pyfury.Fury(ref_tracking=True)

    def serialize(self, obj):
        self.fury_inst.register_class(SerializableQueue, type_tag="serializable_collections.serialzablequeue.SerializableQueue")
        self.fury_inst.register_class(SimpleClass, type_tag="test_class.simple_class.SimpleClass")
        self.fury_inst.register_class(deque, type_tag="_collections.deque")
        # self.fury_inst.register_class(Condition, type_tag="threading.Condition")
        # self.fury_inst.register_class(RLock, type_tag="_thread.RLock")
        return self.fury_inst.serialize(obj)

    def deserialize(self, data):
        return self.fury_inst.deserialize(data)
