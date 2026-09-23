import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# -------------------------------------------------
# Smart Reminder - Machine Learning Model
# -------------------------------------------------

# Training dataset
data = {
    "type": [
        "Medicine", "Medicine", "Medicine",
        "Exam", "Exam", "Exam",
        "Meeting", "Meeting", "Meeting",
        "Workout", "Workout", "Workout"
    ],
    "importance": [
        3, 2, 1,
        3, 2, 1,
        3, 2, 1,
        3, 2, 1
    ],
    "days_left": [
        0, 2, 7,
        1, 3, 10,
        0, 2, 7,
        1, 4, 10
    ],
    "priority": [
        "High", "Medium", "Low",
        "High", "Medium", "Low",
        "High", "Medium", "Low",
        "High", "Medium", "Low"
    ]
}

df = pd.DataFrame(data)

# Convert reminder type into numbers
type_mapping = {
    "Medicine": 0,
    "Exam": 1,
    "Meeting": 2,
    "Workout": 3
}

df["type"] = df["type"].map(type_mapping)

# Features and target
X = df[["type", "importance", "days_left"]]
y = df["priority"]

# Train Machine Learning model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)


# -------------------------------------------------
# Streamlit Interface
# -------------------------------------------------

st.set_page_config(
    page_title="Smart Reminder",
    page_icon="🔔",
    layout="centered"
)

st.title("🔔 Smart Reminder")
st.subheader("ML-Based Reminder Priority Prediction")

st.write(
    "Enter your reminder details below. "
    "The machine learning model will predict the priority "
    "of your reminder."
)

st.divider()

# Reminder type
reminder_type = st.selectbox(
    "📌 Select Reminder Type",
    ["Medicine", "Exam", "Meeting", "Workout"]
)

# Importance
importance = st.slider(
    "⭐ Importance Level",
    min_value=1,
    max_value=3,
    value=2
)

st.caption("1 = Low Importance | 2 = Medium Importance | 3 = High Importance")

# Days remaining
days_left = st.number_input(
    "📅 Days Remaining",
    min_value=0,
    max_value=30,
    value=2
)

st.write("")

# Prediction button
if st.button("🔮 Predict Reminder Priority", use_container_width=True):

    type_value = type_mapping[reminder_type]

    input_data = [[
        type_value,
        importance,
        days_left
    ]]

    prediction = model.predict(input_data)[0]

    st.divider()

    if prediction == "High":
        st.error("🔴 HIGH PRIORITY")
        st.write("⚠️ This reminder should be handled immediately.")

    elif prediction == "Medium":
        st.warning("🟡 MEDIUM PRIORITY")
        st.write("⏰ This reminder should be handled soon.")

    else:
        st.success("🟢 LOW PRIORITY")
        st.write("✅ This reminder can be handled later.")

    st.info(
        f"**Reminder:** {reminder_type}  \n"
        f"**Days Remaining:** {days_left}  \n"
        f"**Importance:** {importance}/3"
    )

st.divider()

st.caption("Smart Reminder | Machine Learning Mini Project")
