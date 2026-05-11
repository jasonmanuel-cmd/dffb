# Investor Tracker — Usage Instructions

Live CSV for tracking investor conversations, meetings, and progress through pipeline stages.

---

## What This Tracker Does

- **Centralized record:** All investor conversations in one place
- **Pipeline visibility:** See at a glance who is where in the funnel
- **Follow-up cadence:** Alerts for next steps and follow-up dates
- **Progress tracking:** Convert contact → coffee call → pitch meeting → term sheet → close
- **Relationship history:** Reference past conversations, interests, timelines

---

## Column Definitions

| Column | Definition | Example |
|--------|-----------|---------|
| **Investor Name** | Full name of investor contact | Jane Smith |
| **Organization** | Fund or company name | Healthcare Partners Fund |
| **Fund Type** | Type of investor (Healthcare Fund, Family Office, VC, Angel, etc.) | Healthcare Fund |
| **Location** | City and state of investor/firm | Boston, MA |
| **Check Size** | Typical investment range (from discussions or research) | $2–5M |
| **Contact Email** | Primary email for investor | jane@hcf.com |
| **Contact Phone** | Primary phone number | 617-555-0101 |
| **Website** | Firm website for reference | www.hcf.com |
| **Date Contacted** | First date you made contact | 2024-01-15 |
| **Contact Channel** | How you reached them (cold email, warm intro, event, LinkedIn, etc.) | Warm intro |
| **Initial Response** | How they responded to initial outreach | "Positive; interested in property example" |
| **First Meeting Date** | Date of first call/meeting | 2024-02-01 |
| **Meeting Type** | Format (phone call, video call, in-person, etc.) | Video call - 45 min |
| **Interest Level** | High / Medium / Low (current assessment) | High |
| **Next Step** | What needs to happen next (send materials, ref call, board discussion, etc.) | Send financial model; request ref call |
| **Next Meeting Date** | When you're scheduled to reconnect | 2024-02-15 |
| **Status** | Pipeline stage (see below) | In Conversation |
| **Notes** | Any relevant context, red flags, or opportunities | "Strong healthcare background; knows operators; board seat potential" |
| **Follow-up Due** | Auto-reminder date for next action | 2024-02-08 |
| **Updated Date** | Last time this row was updated | 2024-02-01 |

---

## Pipeline Statuses

Use these standardized statuses to segment your pipeline:

### **Prospecting Phase**
- **Outreach – No Response:** Initial contact made; no response yet. Follow-up needed.
- **Outreach – Follow-up:** Initial contact made; waiting for response to follow-up. Continue cadence.
- **Outreach – Passed:** Contacted; confirmed not a fit. Mark to deprioritize.

### **Engagement Phase**
- **In Conversation:** Active dialogue; working through initial questions and interest validation.
- **Interested – Pending:** Expressed interest; waiting on materials (financials, data, etc.) or internal review.
- **Low Priority:** Initially interested but lower priority vs. other investors; revisit if needed.

### **Advanced Phase**
- **In Diligence:** Actively reviewing materials; asking detailed questions. May be moving toward term sheet.
- **Term Sheet – Proposed:** Term sheet proposed; waiting for investor response or negotiation.
- **Term Sheet – Negotiating:** Term sheet in negotiation; working on terms.
- **Committed:** Investor has committed capital; working on legal close.

### **Closed**
- **Closed – Funded:** Investment complete; capital received.
- **Passed – Fit Issues:** Investor passed; not a good fit (different thesis, terms, etc.).

---

## Workflow: How to Use This Tracker

### 1. **Sourcing New Investors**
- Add new row for each prospect
- Fill: Name, Organization, Fund Type, Location, Check Size, Email, Website, Date Contacted
- Status: "Outreach – No Response"
- Set Follow-up Due date

### 2. **First Outreach & Response**
- Update Contact Channel (how you reached them)
- Update Initial Response (what they said)
- Update Status based on response
- Set Next Meeting Date if scheduled

### 3. **Meetings & Conversations**
- Add First Meeting Date
- Add Meeting Type and Interest Level
- Update Notes with key takeaways
- Add Next Step (what materials/actions needed)

### 4. **Follow-up & Nurture**
- Check Follow-up Due column daily/weekly
- Send materials, schedule calls, answer questions
- Update Status and Next Meeting Date after each interaction
- Keep Notes current with latest developments

### 5. **Tracking Progress**
- Filter by Status to see pipeline view
- Sort by Next Meeting Date to prioritize follow-ups
- Sort by Interest Level (High → Medium → Low) to focus effort
- Monthly review: which investors are advancing? Which are stalled?

---

## Key Metrics to Track

**Using this CSV, you can measure:**

1. **Pipeline velocity:** How long from first contact to meeting? (Average: 1–2 weeks)
2. **Conversion rates:** What % of contacts → meetings? (Target: 20–30% of cold outreach; 50%+ of warm intros)
3. **Interest progression:** What % move from Medium → High interest? (Target: 30–40%)
4. **Time to term sheet:** How long from first meeting to term sheet discussion? (Target: 4–8 weeks)
5. **Total committed capital:** Sum of investments in "Committed" and "Closed" status

**Monthly reporting template:**
- Total investors contacted: [X]
- Meetings this month: [X]
- Status breakdown: [# Outreach] / [# In Conversation] / [# In Diligence] / [# Term Sheet] / [# Committed]
- Capital pipeline (likely to close): $[X]M
- Capital committed: $[X]M

---

## Tips for Effective Use

### 1. **Update Regularly**
- After every call/email, update the row immediately
- Don't let the tracker get stale; it's only useful if current
- Aim for same-day updates if possible

### 2. **Use Next Step & Follow-up Due Strategically**
- Be specific in Next Step: "Send model + ref call with operator Jane" (not vague "follow up")
- Set Follow-up Due 2–3 days before you actually need to follow up (buffer for action)
- Check Follow-up Due every Monday morning

### 3. **Personalize Notes**
- Reference details from conversations: "Investor mentioned family member in senior care"
- Flag concerns: "Asked about management team depth; may need COO in place"
- Highlight opportunities: "Knows 5+ other potential investors; could syndicate"

### 4. **Segment Your Pipeline**
- Filter by Status to see at-a-glance pipeline health
- Filter by Fund Type to identify which investor segments are most responsive
- Sort by Interest Level to prioritize conversations

### 5. **Don't Neglect Medium/Low Interest Investors**
- Many become High interest after additional data or conversations
- Keep a gentle 4–6 week follow-up cadence even on Medium interest
- Often the best investors are ones who need more convincing initially

### 6. **Use for Board/Advisor Updates**
- Export or share filtered view with advisors to solicit intros
- Monthly board update: "Here's our investor pipeline and progress"
- Builds confidence in fundraising progress

---

## Excel / Google Sheets Tips

### **Import as Google Sheet:**
1. Save CSV as .xlsx (Excel format)
2. Upload to Google Drive
3. Right-click → "Open with" → Google Sheets
4. Share with team for real-time collaboration
5. Set up alerts: Data → Validation → Custom formula to highlight "Follow-up Due" dates

### **Create Useful Views:**
- **Pivot table:** Group by Status to see pipeline breakdown
- **Conditional formatting:** Color code by Interest Level (Green=High, Yellow=Medium, Red=Low)
- **Filter:** Show only "In Conversation" status to see active investors
- **Sort:** By "Follow-up Due" to see who needs attention this week

### **Automation (Google Sheets):**
- Add column: "Days in Pipeline" = TODAY() - Date Contacted
- Add column: "Contact Overdue?" = IF(TODAY() > Follow-up Due, "YES", "NO")
- Set up conditional formatting to highlight overdue contacts in red

---

## Sample Outreach Cadence

**Use this tracker to enforce a consistent follow-up rhythm:**

| Stage | Days Since Contact | Action |
|-------|-------------------|--------|
| 0 days | Initial outreach sent | Update Status: "Outreach – No Response" |
| 5 days | No response | Send follow-up email; set Follow-up Due: Day 12 |
| 12 days | Still no response | Make brief phone call if possible; set Follow-up Due: Day 21 |
| 21 days | No response | Final email + note "attempted 3x; deprioritize" |
| Any day | Response received | Schedule call within 48 hours; update Status |
| Post-call | After meeting | Update notes, Interest Level, Next Step, Next Meeting Date |

---

## Monthly Review Process

**First Monday of each month:**
1. **Open tracker** and review all rows
2. **Update statuses:** Anything that has advanced or stalled?
3. **Count pipeline:** How many investors in each stage?
4. **Calculate capital:** Sum committed + term sheet stage = likely close
5. **Identify stalled:** Any "In Conversation" investors with Follow-up Due >1 month ago? Re-engage or deprioritize.
6. **Report:** Share summary with team/advisors
7. **Forecast:** Based on current pipeline, will you hit capital goal by target date?

---

## Integration with Other Systems

**This tracker works best alongside:**
- Calendar: Block 15–30 min weekly for investor follow-ups (use "Follow-up Due" to identify who needs attention)
- Email templates: Use templated responses for different investor types (saves time, maintains consistency)
- Investor materials folder: Link to shared folder with pitch deck, one-pagers, etc.
- CRM (optional): For larger pipeline (20+ investors), consider moving to CRM like Pipedrive or HubSpot

---

## Red Flags to Watch For

- **"In Conversation" for 8+ weeks:** Likely stalled; needs re-engagement or deprioritization
- **Interest Level declining:** If investor goes from High → Medium, investigate why (timeline? fit? concerns?)
- **Advisor/reference calls not happening:** If investor asks for refs but doesn't follow up, lower priority
- **Too many "Low Priority" investors:** Risk of wasted effort; focus on High interest instead
