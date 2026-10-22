import streamlit as st
import base64
from pathlib import Path


def header_home():

    logo_path = Path(__file__).resolve().parent.parent / "ui" / "student_logo.png"
    with open(logo_path, "rb") as image_file:
        logo_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    st.markdown(
        f"""
       <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 30px;
            margin-bottom: 30px;
        ">
            <img
                src="data:image/png;base64,{logo_base64}"
                style="height: 100px;">
            <h1 style="
                text-align: center;
                color: #E0E3FF;
            ">
                SNAP<br>CLASS
            </h1>
        """,
        unsafe_allow_html=True
    )

def header_dashboard():

    logo_path = Path(__file__).resolve().parent.parent / "ui" / "student_logo.png"
    with open(logo_path, "rb") as image_file:
        logo_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    st.markdown(
        f"""
       <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            gap:10px;
         ">
            <img
                src="data:image/png;base64,{logo_base64}"
                style="height: 85px;">
            <h2 style="
                text-align:left;
                color:#5865F2;
            ">
                SNAP<br>CLASS
            </h2>
        """,
        unsafe_allow_html=True
    )