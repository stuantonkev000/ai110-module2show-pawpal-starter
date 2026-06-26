"""PawPal - pet care daily plan generator.

Class skeleton based on diagrams/uml.mmd. Method bodies are stubbed
out for now; fill them in as you build the app.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, time


@dataclass
class Task:
    """A single care task derived from a pet's needs."""

    name: str
    needed: bool = False
    duration: int | None = None        # minutes
    intensity: str | None = None
    quantity: int | None = None
    notes: str = ""


@dataclass
class PetInfo:
    """Holds whether the pet needs each kind of care, plus details."""

    needs_walks: bool = False
    needs_feeding: bool = False
    needs_meds: bool = False
    needs_enrichment: bool = False
    needs_grooming: bool = False

    walk_duration: int | None = None       # minutes
    walk_intensity: str | None = None
    feeding_quantity: int | None = None
    meds_notes: str = ""
    special_notes: str = ""

    tasks: list[Task] = field(default_factory=list)

    def add_task(self, name: str, needed: bool, **details) -> None:
        """Register a custom/unique task for this pet."""
        raise NotImplementedError

    def get_tasks(self) -> list[Task]:
        """Return all tasks this pet needs."""
        raise NotImplementedError


@dataclass
class Pet:
    """Top-level pet object; owns its PetInfo."""

    name: str
    breed: str
    info: PetInfo = field(default_factory=PetInfo)


@dataclass
class OwnerConstraints:
    """The owner's schedule, preferences, and task priorities."""

    available_times: list[str] = field(default_factory=list)
    preferred_walk_time: time | None = None
    task_priority: dict[str, int] = field(default_factory=dict)
    owner_preferences: str = ""

    def get_priority(self, task: str) -> int:
        """Return the priority ranking for a given task."""
        raise NotImplementedError


@dataclass
class ScheduledTask:
    """A task placed at a specific time in the day's plan."""

    task: Task
    start_time: time | None = None


@dataclass
class Schedule:
    """Generates the day's plan from pet info and owner constraints."""

    day: date | None = None
    plan: list[ScheduledTask] = field(default_factory=list)

    def generate_plan(
        self, pet_info: PetInfo, constraints: OwnerConstraints
    ) -> list[ScheduledTask]:
        """Build the day's plan. Reads pet_info and constraints only."""
        raise NotImplementedError

    def print(self) -> None:
        """Print the generated plan."""
        raise NotImplementedError
