import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load training data
df = pd.read_csv("data/ats_training_data.csv")

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

def predict_pass_probability(core, optional, project, education, structure, tools):
    """
    Predict ATS pass probability for ONE resume
    """
    input_df = pd.DataFrame([{
        "core": core,
        "optional": optional,
        "project": project,
        "education": education,
        "structure": structure,
        "tools": tools
    }])

    prob = model.predict_proba(input_df)[0][1]
    return round(prob * 100, 2)

