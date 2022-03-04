

# Importing the required packages
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# Function importing Dataset
def importdata():
    balance_data = pd.read_csv('WFH_WFO_dataset.csv',
        sep=',', header=None)

    # Printing the dataswet shape
    print("Dataset Length: ", len(balance_data))
    print("Dataset Shape: ", balance_data.shape)

    # Printing the dataset obseravtions
    print("Dataset: ", balance_data.head())
    return balance_data


# Function to split the dataset
def splitdataset(balance_data,col_no):
    # Separating the target variable

    X = balance_data.values[1:, [2,3,4,5,6,10]]
    Y = balance_data.values[1:, col_no]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("Training split input- ", X_train.shape)
    print("Testing split input- ", X_test.shape)

    return X, Y, X_train, X_test, y_train, y_test


# Function to perform training with giniIndex.
def train_using_gini(X_train, y_train):
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini




# Function to make predictions
def prediction(X_test, clf_object):
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix:",
          confusion_matrix(y_test, y_pred))

    print("Accuracy:",
          accuracy_score(y_test, y_pred) * 100)

    print("Classification Report:",
          classification_report(y_test, y_pred))

def train_for_Question(data,column_no):
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data,column_no)
    clf_gini = train_using_gini(X_train, y_train)

    # Operational Phase
    print("Results Using Gini Index:")

    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)


# Driver code
def main():
    # Building Phase
    data = importdata()
    print("Would the Employees Prefer WFH or NOT")
    train_for_Question(data, -1)
    print("Would the Employee be productive while Working from home")
    train_for_Question(data, 13)
    print("Would the Employee have better work life balance")
    train_for_Question(data, 15)

# Calling main function
if __name__ == "__main__":
    main()



def get_correlation_matrix(data, df):
    rows = df['ID'].size
    df['WFH'] = [1] * rows
    print(data.head)
    corrMatrix = df.corr()
    print(corrMatrix)
    plt.figure(figsize=(8, 8))
    sn.heatmap(corrMatrix, annot=True)
    plt.title("Heatmap for India Combined Data")
    plt.show()

