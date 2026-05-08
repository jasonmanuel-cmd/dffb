#!/usr/bin/env python3
"""
Lighthouse mobile performance audit runner with detailed metrics extraction.
"""
import json
import subprocess
import sys
from pathlib import Path

def run_lighthouse():
    """Run Lighthouse audit via Node subprocess and parse results."""
    repo_root = Path(__file__).parent
    report_path = repo_root / "lighthouse-report.json"
    index_url = f"file:///{repo_root}/index.html".replace('\\', '/')
    
    print(f"🔍 Running Lighthouse mobile audit on: {index_url}\n")
    
    cmd = [
        "npx", "lighthouse",
        index_url,
        "--form-factor=mobile",
        "--throttling-method=simulate",
        "--output=json",
        f"--output-path={report_path}",
        "--quiet"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=False, text=True, timeout=180)
        if result.returncode != 0:
            print(f"⚠️  Lighthouse exited with code {result.returncode} (temp cleanup issue, but audit may have run)")
    except subprocess.TimeoutExpired:
        print("❌ Lighthouse timeout after 3 minutes")
        return None
    except FileNotFoundError:
        print("❌ Lighthouse not found. Install with: npm install -g lighthouse")
        return None
    
    # Try to read the report even if the process failed
    if report_path.exists():
        print(f"\n✓ Report generated: {report_path}\n")
        try:
            with open(report_path, 'r') as f:
                report = json.load(f)
            return report
        except json.JSONDecodeError:
            print("❌ Report file exists but is not valid JSON")
            return None
    else:
        print(f"❌ Report file not found at {report_path}")
        return None

def extract_metrics(report):
    """Extract and display key performance metrics."""
    if not report or 'lighthouseResult' not in report:
        print("❌ Invalid report structure")
        return
    
    result = report['lighthouseResult']
    categories = result.get('categories', {})
    audits = result.get('audits', {})
    
    print("=" * 70)
    print("LIGHTHOUSE MOBILE PERFORMANCE AUDIT RESULTS")
    print("=" * 70)
    print()
    
    # Performance score
    perf_cat = categories.get('performance', {})
    perf_score = perf_cat.get('score', 0)
    print(f"📊 Performance Score: {int(perf_score * 100)}/100")
    print()
    
    # Core Web Vitals
    print("Core Web Vitals:")
    print("-" * 70)
    
    lcp = audits.get('largest-contentful-paint', {})
    lcp_val = lcp.get('numericValue')
    lcp_display = lcp.get('displayValue', 'N/A')
    print(f"  • Largest Contentful Paint (LCP): {lcp_display}")
    
    cls = audits.get('cumulative-layout-shift', {})
    cls_val = cls.get('numericValue')
    cls_display = cls.get('displayValue', 'N/A')
    print(f"  • Cumulative Layout Shift (CLS):  {cls_display}")
    
    fid = audits.get('first-input-delay', {})
    if not fid:
        fid = audits.get('total-blocking-time', {})
    fid_display = fid.get('displayValue', 'N/A')
    print(f"  • First Input Delay / TBT:         {fid_display}")
    print()
    
    # Other key metrics
    print("Additional Metrics:")
    print("-" * 70)
    
    fcp = audits.get('first-contentful-paint', {})
    fcp_display = fcp.get('displayValue', 'N/A')
    print(f"  • First Contentful Paint (FCP):   {fcp_display}")
    
    ttfb = audits.get('time-to-first-byte', {})
    ttfb_display = ttfb.get('displayValue', 'N/A')
    print(f"  • Time to First Byte (TTFB):      {ttfb_display}")
    
    tti = audits.get('interactive', {})
    tti_display = tti.get('displayValue', 'N/A')
    print(f"  • Time to Interactive (TTI):      {tti_display}")
    print()
    
    # Opportunities (ranked by impact)
    print("Top Opportunities (ranked by impact):")
    print("-" * 70)
    
    opportunities = []
    for audit_id, audit in audits.items():
        if audit.get('scoreDisplayMode') == 'numeric' and 'savings' in audit:
            impact = audit.get('savings', {}).get('bytes', 0) or 0
            if impact > 0:
                opportunities.append({
                    'title': audit.get('title', audit_id),
                    'description': audit.get('description', ''),
                    'savings': impact,
                    'displayValue': audit.get('displayValue', ''),
                    'score': audit.get('score', 0)
                })
    
    opportunities.sort(key=lambda x: x['savings'], reverse=True)
    
    for i, opp in enumerate(opportunities[:10], 1):
        savings_kb = opp['savings'] / 1024
        print(f"\n  {i}. {opp['title']}")
        print(f"     Potential savings: ~{savings_kb:.1f} KB")
        if opp['displayValue']:
            print(f"     Current value: {opp['displayValue']}")
    
    print("\n" + "=" * 70)
    print(f"Full report saved to: lighthouse-report.json")
    print("=" * 70)

if __name__ == '__main__':
    report = run_lighthouse()
    if report:
        extract_metrics(report)
    else:
        sys.exit(1)
