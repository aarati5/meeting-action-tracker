import json
import os
from datetime import datetime

STORAGE_FILE = "action_items.json"

def load_items() -> list:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def save_items(items: list):
    with open(STORAGE_FILE, "w") as f:
        json.dump(items, f, indent=2)

def add_new_items(new_items: list):
    existing = load_items()
    for item in new_items:
        item["status"] = "pending"
        item["added_on"] = datetime.now().strftime("%Y-%m-%d")
    existing.extend(new_items)
    save_items(existing)
    return existing

def mark_complete(index: int):
    items = load_items()
    if 0 <= index < len(items):
        items[index]["status"] = "completed"
        save_items(items)
        return True
    return False

def get_pending_items() -> list:
    items = load_items()
    return [item for item in items if item["status"] == "pending"]

def get_summary_text() -> str:
    pending = get_pending_items()
    if not pending:
        return "No pending action items."

    lines = ["Pending action items from previous meetings:"]
    for i, item in enumerate(pending):
        lines.append(f"{i+1}. {item['task']} (Owner: {item['owner']}, Deadline: {item['deadline']})")
    return "\n".join(lines)