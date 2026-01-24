import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

students = 50

df = pd.DataFrame({
    "Student_ID": range(1, students + 1),
    "Gender": np.random.choice(["Male", "Female"], students),
    "Maths": np.random.randint(35, 100, students),
    "Science": np.random.randint(30, 100, students),
    "English": np.random.randint(40, 100, students),
    "Attendance": np.random.randint(60, 100, students)
})

df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Percentage"] = df["Total"] / 3

def grade(p):
    if p >= 80:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Percentage"].apply(grade)

print(df.head())


avg_marks = df[["Maths", "Science", "English"]].mean()

plt.figure()
avg_marks.plot(kind="bar")
plt.title("Average Marks per Subject")
plt.ylabel("Marks")
plt.xlabel("Subjects")
plt.show()

plt.figure()
plt.plot(df["Student_ID"], df["Percentage"])
plt.title("Student-wise Percentage Trend")
plt.xlabel("Student ID")
plt.ylabel("Percentage")
plt.show()

plt.figure()
plt.hist(df["Percentage"], bins=10)
plt.title("Percentage Distribution")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.show()

grade_counts = df["Grade"].value_counts()

plt.figure()
plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.show()

plt.figure()
sns.boxplot(x="Gender", y="Percentage", data=df)
plt.title("Gender vs Percentage")
plt.show()

plt.figure()
plt.scatter(df["Attendance"], df["Percentage"])
plt.title("Attendance vs Percentage")
plt.xlabel("Attendance")
plt.ylabel("Percentage")
plt.show()

plt.figure()
sns.heatmap(df[["Maths", "Science", "English", "Attendance", "Percentage"]].corr(),
            annot=True)
plt.title("Correlation Heatmap")
plt.show()

plt.figure()
sns.countplot(x="Grade", data=df)
plt.title("Number of Students per Grade")
plt.show()