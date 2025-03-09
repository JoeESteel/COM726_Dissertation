import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define task data
data = {
    "Task": [
        "Literature Review and Refinement of Research Question",
        "Data Collection and Preprocessing",
        "Development of Baseline Analysis",
        "AI Model Development (Clustering & Anomaly Detection)",
        "Regression and Correlation Analysis",
        "Dashboard Development and Visualisation",
        "Pilot Data Analysis and Interim Review",
        "Comprehensive Data Analysis",
        "Validation and Evaluation",
        "Dissertation Writing - Introduction and Literature Review",
        "Dissertation Writing - Methodology and Data Analysis",
        "Dissertation Writing - Results and Discussion",
        "Dissertation Writing - Conclusion and Recommendations",
        "Final Revisions and Proofreading",
        "Submission Preparation and Turnitin Upload"
    ],
    "Start Date": pd.to_datetime([
        "2025-02-01", "2025-03-10", "2025-03-24", "2025-04-07", "2025-04-21",
        "2025-05-05", "2025-05-23", "2025-06-10", "2025-07-01", "2025-07-15",
        "2025-07-29", "2025-08-12", "2025-08-19", "2025-08-26", "2025-08-31"
    ]),
    "End Date": pd.to_datetime([
        "2025-03-09", "2025-03-23", "2025-04-06", "2025-04-20", "2025-05-04",
        "2025-05-22", "2025-06-09", "2025-06-30", "2025-07-14", "2025-07-28",
        "2025-08-11", "2025-08-18", "2025-08-25", "2025-08-30", "2025-09-01"
    ])
}

# Create DataFrame
df = pd.DataFrame(data)

# Reverse task order
df = df[::-1].reset_index(drop=True)

# Plot Gantt Chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars for each task
for i, task in df.iterrows():
    ax.barh(task["Task"], (task["End Date"] - task["Start Date"]).days, left=task["Start Date"], color='skyblue')

# Formatting X-axis for months and weeks
ax.xaxis.set_major_locator(mdates.MonthLocator())  # Major ticks for months
ax.xaxis.set_minor_locator(mdates.WeekdayLocator())  # Minor ticks for weeks
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Format as Month Year

# Labels and Title
ax.set_xlabel("Timeline")
ax.set_ylabel("Tasks")
ax.set_title("Dissertation Gantt Chart")

# Rotate X-axis labels for clarity
plt.xticks(rotation=45)

# Add grid for better readability
plt.grid(axis='x', linestyle='--', linewidth=0.5)

plt.tight_layout()

# Show the Gantt chart
plt.show()
