import streamlit as st
import joblib
import pandas as pd

# ---------------------- بارگذاری مدل ----------------------
model = joblib.load('finalized_model.sav')
model_columns = joblib.load("model_features.pkl")
feature_columns = ["Area", "Room", "Parking", "Warehouse", "Elevator"]
address_columns = [col for col in model_columns if col not in feature_columns]

# ---------------------- تنظیمات صفحه ----------------------
st.title("💰 پیش‌بینی قیمت ملک")

st.markdown("مدل بر اساس ویژگی‌های واردشده، قیمت ملک را پیش‌بینی می‌کند.")

# ---------------------- ورودی‌های کاربر ----------------------
area = st.number_input("Area")
room = st.number_input("Room")
parking = st.selectbox("Parking", ["True", "False"])
warehouse = st.selectbox("Warehouse", ["True", "False"])
elevator = st.selectbox("Elevator", ["True", "False"])

address_options = [col for col in address_columns]
address = st.sidebar.selectbox("Address", address_options)
input_dict = {col: 0 for col in address_columns}
input_dict[f"{address}"] = 1


# ---------------------- ساخت DataFrame ----------------------
data = pd.DataFrame([{
    "Area": area,
    "Room": room,
    "Parking": 1 if parking == "True" else 0,
    "Warehouse": 1 if warehouse == "True" else 0,
    "Elevator": 1 if elevator == "True" else 0,
    **input_dict
}])

st.write("ورودی شما:")
st.dataframe(data)

# ---------------------- پیش‌بینی ----------------------
if st.button("پیش‌بینی قیمت"):
    prediction = model.predict(data)[0]
    st.success(f"🏠 قیمت پیش‌بینی‌شده: {prediction:,.0f} ")

