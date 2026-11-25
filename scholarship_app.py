
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

st.set_page_config(page_title="AI Scholarship Assistant", page_icon="🎓")

st.title("🎓 AI Scholarship & Education Notice Assistant")
st.write("Understand scholarship notices and check your eligibility in simple English.")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key missing. Please check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

st.header("1. Understand a Scholarship Notice")

notice = st.text_area(
    "Paste your scholarship or education notice here:",
    height=200
)

if st.button("Explain Notice"):
    if not notice.strip():
        st.warning("Please paste a notice first.")
    else:
        with st.spinner("Reading and explaining the notice..."):
            prompt = f"""
            Explain this scholarship notice in very simple English.

            Use these headings:
            1. Purpose of the scholarship
            2. Who can apply?
            3. Required documents
            4. Important dates and deadline
            5. How to apply
            6. Important conditions
            7. Missing information

            Important:
            - Use only information present in the notice.
            - If information is missing, write "Not mentioned in the provided notice".
            - Do not invent dates, eligibility rules or documents.

            Notice:
            {notice}
            """
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )
                st.subheader("Simple Explanation")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()

st.header("2. Student Scholarship Eligibility Checker")

st.write("Enter your details to compare them with the scholarship notice.")

course = st.text_input("Your course / class")
income = st.text_input("Annual family income (in rupees)")
marks = st.text_input("Your marks or percentage")
category = st.text_input("Your category (if applicable)")
state = st.text_input("Your state")

if st.button("Check My Eligibility"):
    if not notice.strip():
        st.warning("Please paste the scholarship notice in Section 1 first.")
    elif not course or not income or not marks:
        st.warning("Please enter at least your course, income and marks.")
    else:
        profile = f"""
        Course/Class: {course}
        Annual family income: {income}
        Marks: {marks}
        Category: {category if category else "Not provided"}
        State: {state if state else "Not provided"}
        """

        prompt = f"""
        You are a careful scholarship eligibility assistant.

        Compare the student profile with the scholarship notice.

        Scholarship notice:
        {notice}

        Student profile:
        {profile}

        Give your answer using these headings:
        1. Eligibility result: ELIGIBLE / NOT ELIGIBLE / CANNOT DETERMINE
        2. Reasons for the result
        3. Conditions satisfied
        4. Conditions not satisfied
        5. Information still required

        Important rules:
        - Use only conditions clearly stated in the notice.
        - Do not invent eligibility rules.
        - If an important condition or student detail is missing,
          choose CANNOT DETERMINE.
        - Explain the result in simple English.
        - This is preliminary guidance, not official approval.
        """

        with st.spinner("Checking your eligibility..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )
                st.subheader("Eligibility Check Result")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.caption("This tool provides preliminary guidance. Always verify details with the official scholarship authority.")
