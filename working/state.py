from typing import TypedDict, List

class AgentState(TypedDict):
    origin: str
    destination: str
    resolved_origin: str
    resolved_dest: str
    graph_path: List[str]
    enhanced_last_mile: str  # Stores the gate exit strategies, modes, and calculated fares
    final_plan: str