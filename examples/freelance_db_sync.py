"""
Example 1: Freelance Offline-First Mobile Invoicing Sync.
Demonstrates solving the data merge conflict vs lock server cost dilemma with Genrikh.
"""

from genrikh.consultant import ConsultantSession, TEMPLATES

def main():
    print("=== Genrikh Case Study: Freelance Offline Mobile Invoicing ===")
    consultant = ConsultantSession()
    report = consultant.run_template("freelancer_offline_sync")
    
    print("\n--- Решение простым языком (Layer 1) ---")
    print(report.result.layer_1)
    
    print("\n--- ТРИЗ-Паспорт решения (Layer 2) ---")
    print(report.result.layer_2)

    with open("freelance_db_sync_report.md", "w", encoding="utf-8") as f:
        f.write(report.to_markdown())
    print("\n✓ Сохранен полный отчет в 'freelance_db_sync_report.md'")

if __name__ == "__main__":
    main()
