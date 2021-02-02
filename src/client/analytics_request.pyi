from enum import Enum
from typing import Any, Dict, Optional

from .primitives.base import BaseTolokaObject


class AnalyticsRequest(BaseTolokaObject):

    class Subject(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class PoolAnalyticsRequest(AnalyticsRequest):

    class Subject(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class RealTasksCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class SubmitedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class SkippedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class RejectedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class ApprovedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class CompletionPercentagePoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class AvgSubmitAssignmentMillisPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class SpentBudgetPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class UniqueWorkersCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class UniqueSubmittersCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str

class ActiveWorkersByFilterCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str, interval_hours: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str
    interval_hours: int

class EstimatedAssignmentsCountPoolAnalytics(PoolAnalyticsRequest):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, subject_id: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    subject_id: str