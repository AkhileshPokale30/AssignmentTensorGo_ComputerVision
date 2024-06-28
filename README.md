# Statistical Analysis and Plotting Application

## Overview

This application performs statistical analysis and generates various plots for a given dataset. It processes student data and visualizes statistics, such as mean, median, mode, standard deviation, and correlation. Additionally, it generates confusion matrices for demonstration purposes. 

## Installation

Follow the steps below to set up and run the application:

1. **Clone the Repository:**
   ```sh
    git clone https://github.com/AkhileshPokale30/AssignmentTensorGo_ComputerVision.git
    cd stat_analysis_app

3. **Install Dependencies:**
   ```sh
    pip install -r requirements.txt


4. **Run the Application:**
   ```sh
    python src/main.py


## Dataset

The dataset used in this application contains student information, including their IDs, scores in various subjects, gender, and class. Here are the columns included in the dataset:

- **Student_ID**: A unique identifier for each student.
- **Maths**: Score in Mathematics.
- **English**: Score in English.
- **Computer**: Score in Computer Science.
- **Gender**: Gender of the student (Male/Female).
- **Class**: Class the student belongs to (e.g., 10A, 10B, 10C).

---

## Generated Reports

Each time the application is run, a new directory is created inside the `plots` directory. The directory name follows the format `run_<n>`, where `<n>` is the run number.

### Combined Histogram Plot

- **File**: `combined_histogram.png`
- **Description**: Displays histograms for Maths, English, and Computer scores in a single image.

### Combined Scatter Plot

- **File**: `combined_scatter.png`
- **Description**: Shows scatter plots for pairs of subjects (Maths vs. English, Maths vs. Computer, English vs. Computer).

### Combined Line Plot

- **File**: `combined_line.png`
- **Description**: Contains line plots for Maths, English, and Computer scores.

### Combined Box Plot

- **File**: `combined_box.png`
- **Description**: Presents box plots for Maths, English, and Computer scores.

### Combined Pie Chart

- **File**: `combined_pie.png`
- **Description**: Displays pie charts for Gender and Class distributions.

### Statistical Plots

- **File**: `statistics.png`
- **Description**: Bar plots for mean, median, mode, and standard deviation, along with a heatmap for correlation coefficients.

### Confusion Matrix

- **File**: `confusion_matrix.png`
- **Description**: Demonstrates a mock confusion matrix for class predictions.

---

## Usage

Upon running the application, the following options will be presented:

1. Plot Histogram
2. Plot Scatter Plot
3. Plot Line Plot
4. Plot Box Plot
5. Plot Pie Chart
6. Ask a Question
7. Exit

### Example

To ask a question, choose option 6 and enter your query. The application integrates with an LLM to provide answers based on the dataset.


## Dependencies

The application requires the following Python packages, which can be installed using the `requirements.txt` file provided in the repository:

- pandas
- matplotlib
- seaborn
- numpy
- scikit-learn

