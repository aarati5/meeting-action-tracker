from src.extractor import extract_action_items
from src.tracker import add_new_items, get_pending_items, get_summary_text, mark_complete

def get_multiline_input(prompt_text):
    print(prompt_text)
    print("(Paste the transcript, then type END on a new line and press Enter)")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def show_menu():
    print("\n" + "=" * 60)
    print("MEETING ACTION-ITEM TRACKER")
    print("=" * 60)
    print("1. Add new meeting transcript")
    print("2. View pending action items")
    print("3. Mark an item as complete")
    print("4. Exit")

def run():
    print(get_summary_text())

    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            transcript = get_multiline_input("\nPaste meeting transcript:")
            print("\nExtracting action items...")
            new_items = extract_action_items(transcript)
            if new_items:
                add_new_items(new_items)
                print(f"\nExtracted {len(new_items)} action item(s):")
                for item in new_items:
                    print(f"  - {item['task']} (Owner: {item['owner']}, Deadline: {item['deadline']})")
            else:
                print("No action items found in this transcript.")

        elif choice == "2":
            pending = get_pending_items()
            if not pending:
                print("\nNo pending action items.")
            else:
                print("\nPending Action Items:")
                for i, item in enumerate(pending):
                    print(f"{i+1}. {item['task']} (Owner: {item['owner']}, Deadline: {item['deadline']})")

        elif choice == "3":
            pending = get_pending_items()
            if not pending:
                print("\nNo pending items to mark complete.")
                continue
            for i, item in enumerate(pending):
                print(f"{i+1}. {item['task']}")
            idx = input("Enter item number to mark complete: ").strip()
            try:
                idx = int(idx) - 1
                if mark_complete(idx):
                    print("Marked as complete.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    run()