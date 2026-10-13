"""
Example 2: Solo Founder 10k RPS Zero-Cost Scaling.
Demonstrates handling viral traffic spikes on a strict $20/month budget ceiling.
"""

from triz.consultant import ConsultantSession, TEMPLATES

def main():
    print("=== TRIZ Side Hustle Case Study: Solo Founder 10k RPS Scale ===")
    consultant = ConsultantSession()
    report = consultant.run_template("solo_founder_scale")
    
    print("\n--- Executive Summary (Layer 1) ---")
    print(report.result.layer_1)
    
    with open("solo_founder_scale_report.md", "w", encoding="utf-8") as f:
        f.write(report.to_markdown())
    print("\n✓ Exported full audit report to 'solo_founder_scale_report.md'")

if __name__ == "__main__":
    main()
