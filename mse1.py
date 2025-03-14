import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Debugging: Print the current working directory
print(f"Current Working Directory: {os.getcwd()}")

try:
    # Read the CSV file
    data = pd.read_csv("iris.csv")  # Replace "iris.csv" with the correct file path if needed
    print("CSV file loaded successfully!")
    
    # Display the first few rows of the dataset
    print("Dataset Preview:")
    print(data.head())

    # Splitting features and labels
    X = data.iloc[:, :-1].values  # All columns except the last (features)
    y = data.iloc[:, -1].values  # The last column (labels)

    # Splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training the k-NN model
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    # Evaluating the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Plotting the Confusion Matrix
    cm = pd.crosstab(y_test, y_pred, rownames=["Actual"], colnames=["Predicted"])
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # Scatter Plot of Sepal Features
    plt.figure(figsize=(6, 4))
    for i, label in enumerate(data.iloc[:, -1].unique()):
        plt.scatter(data[data.iloc[:, -1] == label].iloc[:, 0],
                    data[data.iloc[:, -1] == label].iloc[:, 1],
                    label=label)
    plt.title("Sepal Feature Scatter Plot")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.legend()
    plt.show()

    # Pairplot of All Features
    sns.pairplot(data, hue=data.columns[-1], diag_kind="kde", palette="husl")
    plt.suptitle("Pairplot of All Features", y=1.02)
    plt.show()

    # Boxplot of Each Feature
    plt.figure(figsize=(10, 6))
    for i, column in enumerate(data.columns[:-1]):
        plt.subplot(2, 2, i + 1)
        sns.boxplot(x=data.iloc[:, -1], y=data[column])
        plt.title(f"Boxplot of {column}")
        plt.xlabel("Species")
        plt.ylabel(column)
    plt.tight_layout()
    plt.show()

    # Histogram of Each Feature
    plt.figure(figsize=(10, 6))
    for i, column in enumerate(data.columns[:-1]):
        plt.subplot(2, 2, i + 1)
        plt.hist(data[column], bins=10, alpha=0.7, color='blue', edgecolor='black')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: The specified CSV file was not found. Make sure it exists in the correct directory.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty. Please check the file content.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
