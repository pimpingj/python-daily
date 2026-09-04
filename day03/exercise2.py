def format_date(date):
    year, month, day = [int(n) for n in date.split("-")]
    return f"{year}年{month}月{day}日"

d1 = "2026-09-03"
d2 = "2025-12-25"

print(format_date(d1))
print(format_date(d2))