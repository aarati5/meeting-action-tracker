# Meeting Action-Item Tracker

An AI-powered tool that extracts action items from meeting transcripts and persistently tracks them across sessions — so nothing falls through the cracks between meetings.

## Problem It Solves

Most meeting-summary tools just generate a one-time summary and forget about it. This tool goes a step further: it maintains state across sessions, so when you start a new meeting, you can see what's still pending from before — enabling real accountability tracking, not just note-taking.

## How It Works

1. User pastes a meeting transcript
2. Gemini API extracts structured action items (task, owner, deadline) as JSON, filtering out non-actionable discussion
3. Items are saved to a local JSON file with a "pending" status
4. On the next run, previously pending items are automatically shown at startup
5. Users can view pending items or mark them complete, updating the persistent store

## Tech Stack

- Language: Python
- LLM: Google Gemini API (gemini-3.8-flash)
- Core concept: Structured JSON extraction + persistent state management (no database needed)

## Setup

1. Clone the repo and navigate into it

2. Create a virtual environment:

python -m venv venv
venv\Scripts\activate

3. Install dependencies:

pip install google-generativeai python-dotenv

4. Create a .env file with your Gemini API key:

GEMINI_API_KEY=your_key_here

Get a free key at https://aistudio.google.com/apikey

5. Run the program:

python main.py

## Usage

Run the program and choose from the menu:
1. Add new meeting transcript (paste text, type END on a new line to submit)
2. View pending action items
3. Mark an item as complete
4. Exit

Pending items from previous sessions are shown automatically every time the program starts.

## Example

Input transcript:

Alright team, let's wrap up. Sarah, please finish the API documentation by Friday.
John, you need to review the pull request from Mike before next Monday's release.
We also discussed the new UI design but no decisions were made there.
Also someone needs to update the deployment script, no rush on that one.

Extracted output:
- Finish the API documentation (Owner: Sarah, Deadline: Friday)
- Review the pull request from Mike (Owner: John, Deadline: next Monday)
- Update the deployment script (Owner: unassigned, Deadline: not specified)

Note: the UI design discussion was correctly excluded since it wasn't an actionable item.

## Architecture

main.py - menu-driven CLI loop, connects extraction and tracking
src/extractor.py - calls Gemini API, parses structured JSON action items from raw transcript text
src/tracker.py - persistence layer; reads/writes action_items.json to maintain state across sessions

## Future Improvements

- Add due-date-based reminder notifications
- Support recurring meeting templates that auto-carry-forward unresolved items
- Replace JSON file storage with a proper database for multi-user support
- Add a web UI instead of CLI