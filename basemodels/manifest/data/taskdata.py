from typing_extensions import Literal
from typing import Dict, Callable, Any, Union, Type, ClassVar 
from pydantic import BaseModel, HttpUrl, validate_model, ValidationError
from uuid import UUID
from typing import Optional

class TaskDataEntry(BaseModel):
    """
    Taskdata file format:

    [
      {
        "task_key": "407fdd93-687a-46bb-b578-89eb96b4109d",
        "datapoint_uri": "https://domain.com/file1.jpg",
        "datapoint_hash": "f4acbe8562907183a484498ba901bfe5c5503aaa"
      },
      {
        "task_key": "20bd4f3e-4518-4602-b67a-1d8dfabcce0c",
        "datapoint_uri": "https://domain.com/file2.jpg",
        "datapoint_hash": "f4acbe8562907183a484498ba901bfe5c5503aaa"
      }
    ]
    """
    task_key: UUID
    datapoint_uri: HttpUrl
    datapoint_hash: Optional[str]


def validate_taskdata_entry(value: dict):
    """ Validate taskdata entry """
    if not isinstance(value, dict):
        raise ValidationError("taskdata entry should be dict", TaskDataEntry())

    *_, validation_error = validate_model(TaskDataEntry, value)
    if validation_error:
          raise validation_error
