import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix

def ensure_run_directory(run_id):
    run_path = os.path.join('plots', f'run_{run_id}')
    if not os.path.exists(run_path):
        os.makedirs(run_path)
        print(f"Created '{run_path}' directory.")
    else:
        print(f"'{run_path}' directory already exists.")
    return run_path

def combine_plots(run_path, plot_type, columns, plot_func):
    plt.figure(figsize=(12, 8))
    for i, column in enumerate(columns, 1):
        plt.subplot(2, 2, i)
        plot_func(column)
    plt.tight_layout()
    file_path = os.path.join(run_path, f'combined_{plot_type}.png')
    plt.savefig(file_path)
    if os.path.exists(file_path):
        print(f'Successfully saved combined {plot_type} plot to {file_path}')
    else:
        print(f'Failed to save combined {plot_type} plot to {file_path}')
    plt.close()

def plot_histogram(df, run_path):
    combine_plots(run_path, 'histogram', ['Maths', 'English', 'Computer'], lambda col: df[col].hist())

def plot_scatter(df, run_path):
    def scatter_plot(col1, col2):
        df.plot.scatter(x=col1, y=col2)
        plt.title(f'{col1} vs {col2}')
    plt.figure(figsize=(12, 8))
    scatter_columns = [('Maths', 'English'), ('Maths', 'Computer'), ('English', 'Computer')]
    for i, (col1, col2) in enumerate(scatter_columns, 1):
        plt.subplot(2, 2, i)
        scatter_plot(col1, col2)
    plt.tight_layout()
    file_path = os.path.join(run_path, 'combined_scatter.png')
    plt.savefig(file_path)
    if os.path.exists(file_path):
        print(f'Successfully saved combined scatter plot to {file_path}')
    else:
        print(f'Failed to save combined scatter plot to {file_path}')
    plt.close()

def plot_line(df, run_path):
    combine_plots(run_path, 'line', ['Maths', 'English', 'Computer'], lambda col: df[col].plot.line())

def plot_box(df, run_path):
    combine_plots(run_path, 'box', ['Maths', 'English', 'Computer'], lambda col: df.boxplot(column=[col]))

def plot_pie(df, run_path):
    plt.figure(figsize=(12, 6))
    for i, column in enumerate(['Gender', 'Class'], 1):
        plt.subplot(1, 2, i)
        df[column].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title(f'Pie Chart of {column}')
    plt.tight_layout()
    file_path = os.path.join(run_path, 'combined_pie.png')
    plt.savefig(file_path)
    if os.path.exists(file_path):
        print(f'Successfully saved combined pie chart to {file_path}')
    else:
        print(f'Failed to save combined pie chart to {file_path}')
    plt.close()

def plot_statistics(df, stats, run_path):
    numeric_df = df.select_dtypes(include=[np.number])
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 3, 1)
    numeric_df.mean().plot(kind='bar')
    plt.title('Mean')

    plt.subplot(2, 3, 2)
    numeric_df.median().plot(kind='bar')
    plt.title('Median')

    plt.subplot(2, 3, 3)
    numeric_df.mode().iloc[0].plot(kind='bar')
    plt.title('Mode')

    plt.subplot(2, 3, 4)
    numeric_df.std().plot(kind='bar')
    plt.title('Standard Deviation')

    plt.subplot(2, 3, 5)
    sns.heatmap(numeric_df.corr(), annot=True)
    plt.title('Correlation Coefficient')

    plt.tight_layout()
    file_path = os.path.join(run_path, 'statistics.png')
    plt.savefig(file_path)
    if os.path.exists(file_path):
        print(f'Successfully saved statistics plot to {file_path}')
    else:
        print(f'Failed to save statistics plot to {file_path}')
    plt.close()

def plot_confusion_matrix(df, run_path):
    # For demonstration, we create a mock confusion matrix using random data.
    y_true = np.random.choice(['Class_A', 'Class_B', 'Class_C'], size=100)
    y_pred = np.random.choice(['Class_A', 'Class_B', 'Class_C'], size=100)
    cm = confusion_matrix(y_true, y_pred, labels=['Class_A', 'Class_B', 'Class_C'])
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=['Class_A', 'Class_B', 'Class_C'], yticklabels=['Class_A', 'Class_B', 'Class_C'])
    plt.title('Confusion Matrix')
    file_path = os.path.join(run_path, 'confusion_matrix.png')
    plt.savefig(file_path)
    if os.path.exists(file_path):
        print(f'Successfully saved confusion matrix plot to {file_path}')
    else:
        print(f'Failed to save confusion matrix plot to {file_path}')
    plt.close()
