import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator")
st.write(
    "Body mass index (BMI) is your weight in kilograms divided by the "
    "square of your height in metres (kg/m²)."
)

col1, col2 = st.columns(2)
with col1:
    height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=272.0, value=170.0, step=0.5)
with col2:
    weight_kg = st.number_input("Weight (kg)", min_value=2.0, max_value=650.0, value=65.0, step=0.5)


def bmi_category(bmi: float) -> tuple[str, str]:
    if bmi < 18.5:
        return "Underweight", "warning"
    elif bmi < 25:
        return "Normal weight", "success"
    elif bmi < 30:
        return "Overweight", "warning"
    else:
        return "Obese", "error"


if st.button("Calculate", type="primary", use_container_width=True):
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 1)
    category, level = bmi_category(bmi)

    st.metric("Your BMI", f"{bmi}")
    message = f"BMI = {bmi}: **{category}**"
    getattr(st, level)(message)

with st.expander("BMI categories"):
    st.markdown(
        """
| BMI | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obese |
"""
    )
