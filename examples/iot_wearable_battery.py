"""
Example 3: IoT Medical Wearable Telemetry vs Battery.
Demonstrates achieving continuous patient monitoring on a single coin-cell battery.
"""

from triz.consultant import ConsultantSession, TEMPLATES

def main():
    print("=== TRIZ Side Hustle Case Study: IoT Medical Wearable Battery ===")
    consultant = ConsultantSession()
    report = consultant.run_template("iot_wearable_battery")
    
    print("\n--- Executive Summary (Layer 1) ---")
    print(report.result.layer_1)
    
    with open("iot_wearable_battery_report.md", "w", encoding="utf-8") as f:
        f.write(report.to_markdown())
    print("\n✓ Exported full audit report to 'iot_wearable_battery_report.md'")

if __name__ == "__main__":
    main()
