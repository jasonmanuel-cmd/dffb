#!/usr/bin/env python3
"""Simple CSV updater for operator_responses_live.csv

Usage examples:
  python tools/update_operator_csv.py --operator "Jane" --facility "Care Home" --address "123 Main St" --city "Anytown" --state CA --beds 8 --occupancy 75 --contact "Jane Doe" --email jane@example.com --phone 555-0101 --date 2026-05-11 --channel email --status Contacted --notes "Called, will follow up" --next_step "Send checklist" --next_date 2026-05-18 --owner_age 72 --succession High

This script will create the CSV if missing and append a new row.
"""
import csv
import os
import argparse
from datetime import datetime

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'docs', 'operators', 'operator_responses_live.csv')

HEADERS = [
    'Operator Name', 'Facility Name', 'Address', 'City', 'State', 'Beds', 'Estimated Occupancy (%)',
    'Contact Name', 'Contact Email', 'Contact Phone', 'Date Contacted', 'Channel', 'Status', 'Notes',
    'Next Step', 'Next Contact Date', 'Owner Age', 'Succession Likelihood'
]


def write_header_if_missing(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)


def append_row(args):
    write_header_if_missing(CSV_PATH)
    row = [
        args.operator or '', args.facility or '', args.address or '', args.city or '', args.state or '',
        args.beds or '', args.occupancy or '', args.contact or '', args.email or '', args.phone or '',
        args.date or datetime.utcnow().date().isoformat(), args.channel or '', args.status or '', args.notes or '',
        args.next_step or '', args.next_date or '', args.owner_age or '', args.succession or ''
    ]
    with open(CSV_PATH, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def parse_args():
    p = argparse.ArgumentParser(description='Append a row to operator_responses_live.csv')
    p.add_argument('--operator')
    p.add_argument('--facility')
    p.add_argument('--address')
    p.add_argument('--city')
    p.add_argument('--state')
    p.add_argument('--beds')
    p.add_argument('--occupancy')
    p.add_argument('--contact')
    p.add_argument('--email')
    p.add_argument('--phone')
    p.add_argument('--date')
    p.add_argument('--channel')
    p.add_argument('--status')
    p.add_argument('--notes')
    p.add_argument('--next_step')
    p.add_argument('--next_date')
    p.add_argument('--owner_age')
    p.add_argument('--succession')
    return p.parse_args()


def main():
    args = parse_args()
    append_row(args)
    print('Appended row to', CSV_PATH)


if __name__ == '__main__':
    main()
