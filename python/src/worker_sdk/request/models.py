from typing import List, Optional

from pydantic import BaseModel, StrictStr


# TODO(adrian@preemo.io, 02/01/2023): move to core?
class ImmutableModel(BaseModel):
    class Config:
        allow_mutation = False


# TODO(adrian@preemo.io, 02/01/2023): consider if it makes any sense to recreate these
class RegisteredFunction(ImmutableModel):
    name: StrictStr
    namespace: Optional[StrictStr]


class RegisterFunctionsRequest(ImmutableModel):
    functions_to_register: List[RegisteredFunction]
