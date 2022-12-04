from dataclasses import dataclass
from Cards import Card
from typing import List, Dict, Optional
from SleepingQueens import SleepingQueens
from Cards import Queen


@dataclass
class PlayerState:
    cards: Dict[int, Optional[Card] ]
    awokenQueens: Dict[int, Queen]
