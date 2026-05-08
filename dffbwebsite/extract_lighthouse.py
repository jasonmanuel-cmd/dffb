#!/usr/bin/env python3
"""Extract key metrics from Lighthouse JSON report."""
import json
from pathlib import Path

report_path = Path("lighthouse-report.json")
with open(report_path, 'r') as f:
    report = json.load(f)

result = report['lighthouseResult']
categories = result['categories']
audits = result['audits']

# Performance score
perf_score = categories['performance']['score']
print('=' * 70)
print('LIGHTHOUSE MOBILE PERFORMANCE AUDIT RESULTS')
print('=' * 70)
print()
print(f'📊 Performance Score: {int(perf_score * 100)}/100')
print()

# Core Web Vitals
print('Core Web Vitals:')
print('-' * 70)
print(f"  • Largest Contentful Paint (LCP): {audits['largest-contentful-paint']['displayValue']}")
print(f"  • Cumulative Layout Shift (CLS):  {audits['cumulative-layout-shift']['displayValue']}")
print(f"  • Total Blocking Time (TBT):       {audits['total-blocking-time']['displayValue']}")
print()

# Other key metrics
print('Additional Metrics:')
print('-' * 70)
print(f"  • First Contentful Paint (FCP):   {audits['first-contentful-paint']['displayValue']}")
print(f"  • Server Response Time (TTFB):    {audits['server-response-time']['displayValue']}")
print(f"  • Time to Interactive (TTI):      {audits['interactive']['displayValue']}")
print(f"  • Speed Index:                    {audits['speed-index']['displayValue']}")
print()

# Opportunities (top 10)
opportunities = []
for audit_id, audit in audits.items():
    if audit.get('scoreDisplayMode') == 'numeric' and 'savings' in audit:
        impact = audit.get('savings', {}).get('bytes', 0) if isinstance(audit.get('savings'), dict) else 0
        if impact > 0:
            opportunities.append({
                'title': audit.get('title', audit_id),
                'savings': impact,
                'displayValue': audit.get('displayValue', ''),
            })

opportunities.sort(key=lambda x: x['savings'], reverse=True)

if opportunities:
    print('Top 10 Optimization Opportunities (by byte savings):')
    print('-' * 70)
    for i, opp in enumerate(opportunities[:10], 1):
        savings_kb = opp['savings'] / 1024
        print(f"{i}. {opp['title']}")
        print(f"   Potential savings: ~{savings_kb:.1f} KB")
else:
    print('No optimization opportunities identified.')
    
print()
print('=' * 70)
print('Report file: lighthouse-report.json')
print('=' * 70)
