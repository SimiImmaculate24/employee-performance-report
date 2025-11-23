import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Verification email
VERIF_EMAIL = "24ds2000040@ds.study.iitm.ac.in"

# --- Step 1: create dataset if not found ---
data_file = "employees.csv"
if not os.path.exists(data_file):
    df = pd.DataFrame({
        "employee_id": [f"EMP{i:03d}" for i in range(1, 101)],
        "department": ["R&D","HR","Marketing","Finance","Sales"] * 20,
        "region": ["Asia","Africa","Europe","America","Asia"] * 20,
        "performance_score": [70 + (i % 20) for i in range(100)],
        "years_experience": [i % 15 for i in range(100)],
        "satisfaction_rating": [3 + (i % 2) for i in range(100)],
    })
    df.to_csv(data_file, index=False)
else:
    df = pd.read_csv(data_file)

# --- Step 2: compute frequency count ---
rd_count = df[df["department"] == "R&D"].shape[0]
print("Frequency count for R&D department:", rd_count)

# --- Step 3: plot histogram ---
sns.set(style="whitegrid")
plt.figure(figsize=(8,5))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

# Encode image to base64 for embedding inside HTML
with open("histogram.png", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode("utf-8")

# --- Step 4: embed the Python code inside HTML ---
with open("create_report.py", "r") as f:
    python_code = f.read()

html_content = f"""
<html>
<head>
<title>Employee Performance Report</title>
</head>
<body>
<h1>Employee Performance Report</h1>

<h3>Verification Email:</h3>
<p>{VERIF_EMAIL}</p>

<h3>R&D Department Frequency:</h3>
<p>{rd_count}</p>

<h3>Histogram Visualization:</h3>
<img src="data:image/png;base64,{encoded}" width="600"/>

<h3>Python Code Used:</h3>
<pre><code>
{python_code}
</code></pre>

</body>
</html>
"""

with open("report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("report.html created successfully.")
