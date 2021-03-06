# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class SelfTest(p.MessageType):
    MESSAGE_WIRE_TYPE = 32

    def __init__(
        self,
        payload: bytes = None,
    ) -> None:
        self.payload = payload

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('payload', p.BytesType, 0),
        }
