"""
Programmer: python_scripts (Abhijith Warrier)

PYTHON EVERYDAY — F-Strings: From Messy Output to Clean Reports

Demonstrate how f-strings turn raw values into a readable report using
decimal precision, thousands separators, and column alignment. Formatting
changes the displayed text without changing the original numeric values.

Run: python fstrings_clean_reports.py
Requires Python 3.6+; no third-party packages.
"""

# 1. Sample data: labels and illustrative sizes in kilobytes.
ROWS = [("Images", 12345.678), ("Logs", 987.6), ("Cache", 42.0)]


def build_report(rows):
    """Return a small, plain-text report for a monospaced display."""
    # <10: left-align in a minimum width of 10 characters.
    # >12: right-align in a minimum width of 12 characters.
    lines = [f"{'Folder':<10} {'Size (KB)':>12}", "-" * 23]
    for name, size in rows:
        # , groups thousands; .2f displays two digits after the decimal point.
        lines.append(f"{name:<10} {size:>12,.2f}")
    return "\n".join(lines)


def main():
    # 2. Raw output has uneven columns and decimal precision.
    print("BEFORE")
    for name, size in ROWS:
        print(name, size)

    # 3. A colon introduces formatting rules inside an f-string field.
    size = ROWS[0][1]
    print("\nONE VALUE, STEP BY STEP")
    print(f"Raw:        {size}")       # 12345.678
    print(f"Two places: {size:.2f}")   # 12345.68
    print(f"Grouped:    {size:,.2f}")  # 12,345.68

    # 4. Combine text alignment and numeric formatting into a report.
    print("\nAFTER")
    print(build_report(ROWS))

    # 5. Formatting returns text; the original numeric value is unchanged.
    formatted = f"{size:,.2f}"
    assert formatted == "12,345.68"
    assert size == 12345.678
    assert f"{42.0:,.2f}" == "42.00"
    assert f"{-1234.5:,.2f}" == "-1,234.50"
    assert build_report(ROWS).splitlines()[2] == "Images        12,345.68"

    # Width is a MINIMUM, not a limit: longer content is not truncated.
    assert f"{'VeryLongFolder':<10}" == "VeryLongFolder"
    # Fixed widths suit this small ASCII example; use wider/dynamic fields
    # for longer values. Comma grouping here is not locale-aware.


if __name__ == "__main__":
    main()
