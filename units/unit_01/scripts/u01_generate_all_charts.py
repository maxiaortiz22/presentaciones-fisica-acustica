from u01_chartlib import generate_all


if __name__ == "__main__":
    report = generate_all()
    print(f"Generated {len(report['generated'])} charts.")
    for sheet in report["contact_sheets"]:
        print(f"Contact sheet: {sheet}")
