# Property Lead Tracking — README

## Files

- `properties_target_list.csv` — live list of identified distressed/inherited properties to contact
- `property_leads_tracker.csv` — tracks all conversations, evaluations, and pipeline status

## Quick Usage

### Adding a new target property

Use the Python updater (coming next) or manually add rows to `properties_target_list.csv`:

```
Address | City | State | Est. Value | Condition | Lead Source | Owner | Email | Phone | Date Identified | Status
```

Example statuses:
- `Prospect` — identified but not yet contacted
- `Contacted` — first outreach sent
- `Interested` — owner expressed interest
- `Evaluating` — site visit completed or in progress
- `Negotiating` — terms being discussed
- `Closed-Won` — deal completed
- `Closed-Lost` — owner declined or passed

### Tracking conversations

Use `property_leads_tracker.csv` to log:
- Date and channel of contact (email, call, visit)
- Owner response and next steps
- Viability assessment (Green/Yellow/Red)
- Deal status and estimated close date

### Weekly cadence

1. Pull 5–10 new probate/code enforcement leads from sources
2. Add to `properties_target_list.csv`
3. Initiate contact (email, call, door visit)
4. Log conversations in `property_leads_tracker.csv`
5. Schedule follow-ups for leads showing interest

## Maintenance

- Update status as conversations progress
- Close deals when signed (move to "Closed-Won")
- Document reasons for declined offers ("Closed-Lost")
- Use tracker data to refine messaging and process

## Privacy

Only store name, email, phone, and basic property info in these CSVs. Store detailed personal/financial details in a separate, secure CRM if needed.
