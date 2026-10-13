"""
Example 1: Freelance Offline-First Mobile Invoicing Sync.
Demonstrates solving the data merge conflict vs lock server cost dilemma.
"""

from triz.consultant import ConsultantSession, TEMPLATES

def main():
    print("=== TRIZ Side Hustle Case Study: Freelance Offline Mobile Invoicing ===")
    consultant = ConsultantSession()
    report = consultant.run_template("freelancer_offline_sync")
    
    print("\n--- Executive Summary (Layer 1) ---")
    print(report.result.layer_1)
    
    print("\n--- Methodological TRIZ Passport (Layer 2) ---")
    print(report.result.layer_2)

    # Save to file
    with open("freelance_db_sync_report.md", "w", encoding="utf-8") as f:
        f.write(report.to_markdown())
    print("\n✓ Exported full audit report to 'freelance_db_sync_report.md'")

if __name__ == "__main__":
    main()
