import queue
from typing import Dict, List
from collections import deque
from serializable_collections.serializablequeue import SerializableQueue


class SimpleClass:
    f1: "SimpleClass"
    f2: Dict[str, str]
    f3: Dict[str, str]
    f4: List[str]
    f5: deque
    # __dict__: Dict[str, str]
    f6: SerializableQueue

    def __init__(self):
        self.f4 = []
        self.f5 = deque()
        self.f6 = SerializableQueue()
        # self.__dict__ = {'a': 'a', 'b': 'b1'}

    # def __getstate__(self):
    #     state = self.__dict__.copy()
    #     # del state["f6"]
    #     state['queue'] = self.tool_queue.get(0)
    #     return state
    #
    # def __setstate__(self, state: Dict[str, str]):
    #     self.__dict__.update(state)
    #     self.f6 = queue.Queue()
    #     self.f6.put(1)
