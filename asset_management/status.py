from enum import Enum


class Status(Enum):

    Not_Assigned = 1
    In_Progress = 2
    Needs_Review = 3
    Off_Track = 4
    Reviewed = 5
    Complete = 6
