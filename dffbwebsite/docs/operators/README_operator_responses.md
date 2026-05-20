Operator Responses Live CSV — README
---------------------------------

Files added:
- `docs/operators/operator_responses_live.csv` — live tracker CSV you can open in Excel or upload to Google Sheets
- `tools/update_operator_csv.py` — small script to append rows to the CSV from the command line

Quick usage

1) Local updates (command line):

Run the Python script to append a row (example):

```bash
python tools/update_operator_csv.py --operator "Jane Owner" --facility "Sunset Care" --address "123 Main St" --city "Anytown" --state CA --beds 8 --occupancy 72 --contact "Jane Owner" --email jane@example.com --phone 555-0101 --date 2026-05-11 --channel email --status Contacted --notes "Sent checklist" --next_step "Call" --next_date 2026-05-18 --owner_age 78 --succession High
```

2) Live collaboration via Google Sheets:
- Open Google Sheets, go to `File > Import > Upload` and choose `operator_responses_live.csv`.
- Choose "Replace spreadsheet" or "Append to current sheet" as desired.
- To keep it live, use Google Sheets native sharing and edit there. To persist changes locally, export CSV periodically from Google Sheets.

3) Integrations:
- You can automate appends from other systems by calling `tools/update_operator_csv.py` from scripts or Zapier/Make by executing a small VM or using an intermediary webhook.

Status categories recommended
- Prospect, Contacted, Interested, Pilot, Closed-Won, Closed-Lost, Rejected

Maintenance notes
- The script will create the CSV with headers if it does not exist.
- CSV path is `docs/operators/operator_responses_live.csv` relative to repository root.

Privacy
- Do not commit sensitive personal data (PII) you are not authorized to store in the repository. Use a secure CRM for sensitive details if needed.
