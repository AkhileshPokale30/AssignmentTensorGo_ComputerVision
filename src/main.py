import os
import pandas as pd
from data_reader import read_csv
from stats_analysis import calculate_statistics
from plotting import plot_histogram, plot_scatter, plot_line, plot_box, plot_pie, plot_statistics, plot_confusion_matrix
from llm_integration import initialize_llm, ask_question

def main():
    # Determine the run number by counting existing 'run_' directories
    base_plot_dir = 'plots'
    if not os.path.exists(base_plot_dir):
        os.makedirs(base_plot_dir)
    run_number = len([d for d in os.listdir(base_plot_dir) if d.startswith('run_')]) + 1
    run_path = os.path.join(base_plot_dir, f'run_{run_number}')
    os.makedirs(run_path)
    print(f"Current working directory: {os.getcwd()}")
    print(f"Run directory: {run_path}")

    df = read_csv()
    stats = calculate_statistics(df)
    print("Statistics:", stats)

    llm = initialize_llm()

    plot_histogram(df, run_path)
    plot_scatter(df, run_path)
    plot_line(df, run_path)
    plot_box(df, run_path)
    plot_pie(df, run_path)
    plot_statistics(df, stats, run_path)
    plot_confusion_matrix(df, run_path)

    while True:
        print("\nOptions:")
        print("1. Ask a Question")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            question = input("Enter your question: ")
            answer = ask_question(llm, question)
            print("Answer:", answer)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
