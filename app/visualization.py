import matplotlib.pyplot as plt
import os

def create_histogram(ax, function_lengths, file_name):
    ax.hist(function_lengths, bins=10, color='blue', alpha=0.7)
    ax.set_title('Distribution of Function Lengths')
    ax.set_xlabel('Length of Function (lines)')
    ax.set_ylabel('Frequency')
    plt.savefig(f'graphs/{file_name}_function_lengths_histogram.png')
    # plt.close()

def create_pie_chart(ax, alert_types, file_name):
    ax.pie(alert_types.values(), labels=alert_types.keys(), autopct='%1.1f%%', startangle=140)
    ax.set_title('Alerts by Type')
    plt.savefig(f'graphs/{file_name}_alerts_by_type_pie_chart.png')
    # plt.close()


def create_bar_chart(file_alerts):
    files = list(file_alerts.keys())  # רשימת הקבצים
    counts = list(file_alerts.values())  # מספר הבעיות בכל קובץ
    plt.bar(files, counts, color='red')
    plt.title('Number of Alerts per File')  # הוסף כותרת לתרשים
    plt.ylabel('Count')  # תקן את השימוש ב-plt.ylabel
    plt.xticks(rotation=45)  # סובב את השמות של הקבצים כדי שיהיה קל יותר לקרוא
    plt.tight_layout()  # מתאימה את המרווחים בין הגרפים
    plt.savefig('graphs/_alerts_per_file.png')  # שמור את התרשים
    plt.show()  # הצג את התרשים
    plt.close()  # סגור את התמונה

def create_graphs(alerts, function_lengths, file_name):
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    # 1. היסטוגרמה
    create_histogram(axs[0], function_lengths, file_name)

    # 2. תרשים עוגה
    alert_types = {'Missing Docstring': 0, 'Function Too Long': 0, 'Unused Variables': 0}
    for alert in alerts:
        if "missing a docstring" in alert:
            alert_types['Missing Docstring'] += 1
        elif "longer than 20 lines" in alert:
            alert_types['Function Too Long'] += 1
        elif "never used" in alert:
            alert_types['Unused Variables'] += 1
    create_pie_chart(axs[1], alert_types, file_name)

    plt.tight_layout()
    plt.show()


if not os.path.exists('graphs'):
    os.makedirs('graphs')