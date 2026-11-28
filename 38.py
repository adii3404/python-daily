import time
from dataclasses import dataclass, field
from contextlib import contextmanager

# 1. Dataclasses: Clean data modeling with type hints & auto-methods
@dataclass
class Task:
    id: int
    title: str
    priority: str = "Medium"
    tags: list = field(default_factory=list)
    completed: bool = False

    def mark_done(self):
        self.completed = True


t1 = Task(1, "Review PR #42", priority="High", tags=["backend", "security"])
t2 = Task(2, "Update daily Python notes", tags=["learning"])
t2.mark_done()

print("Task 1:", t1)
print("Task 2 status:", t2.title, "-> Completed:", t2.completed)

print()

# 2. Generator-based Context Manager using contextlib
@contextmanager
def execution_timer(label: str):
    start = time.perf_counter()
    print(f"[{label}] Execution started...")
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] Finished in {elapsed:.4f} seconds.")


with execution_timer("Square computation"):
    total = sum(x * x for x in range(1_000_000))
    print(f"Sum of squares computed: {total}")

print()

# 3. Class-based Context Manager with __enter__ and __exit__
class TempSettings:
    """Safely overrides and restores a dictionary setting."""

    def __init__(self, settings_dict: dict, key: str, temp_value):
        self.settings = settings_dict
        self.key = key
        self.temp_value = temp_value
        self.previous_value = None

    def __enter__(self):
        self.previous_value = self.settings.get(self.key)
        self.settings[self.key] = self.temp_value
        print(f"Overridden '{self.key}': {self.previous_value} -> {self.temp_value}")
        return self.settings

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.settings[self.key] = self.previous_value
        print(f"Restored '{self.key}' back to: {self.previous_value}")


app_config = {"debug": False, "version": "1.0.0"}
print("Config before:", app_config)

with TempSettings(app_config, "debug", True):
    print("Inside context block config:", app_config)

print("Config after block:", app_config)
