import pandas as pd

data = {
    "الاسم": ["هدى", "أحمد", "سارة"],
    "العمر": [23, 30, 25],
    "المدينة": ["دمشق", "حلب", "اللاذقية"]
}

df = pd.DataFrame(data)
print(df)
print("\n--- إحصائيات الأعمار ---")
print(df["العمر"].mean())