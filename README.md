
# AI Scholarship & Education Notice Assistant

An AI-powered application that helps students understand scholarship notifications and check their preliminary eligibility using Google Gemini.

## Project Overview

Scholarship notifications often contain complicated eligibility conditions, income limits, required documents, and application deadlines.

This application uses a Large Language Model (LLM) to explain scholarship notices in simple English and compare student details with the conditions mentioned in the notice.

## Features

1. **Scholarship Notice Explanation**
   - Explains scholarship notices in simple English.
   - Identifies eligibility conditions, required documents, and deadlines.
   - Highlights information that is missing from the notice.

2. **Student Eligibility Checker**
   - Accepts student details such as course, family income, marks, category, and state.
   - Compares student details with scholarship conditions.
   - Provides ELIGIBLE, NOT ELIGIBLE, or CANNOT DETERMINE results.
   - Explains the reasons behind the result.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- Python Dotenv

## Installation and Execution

1. Clone this repository.
2. Install the required packages:

   `pip install -r requirements.txt`

3. Create a `.env` file in the project folder and add your Gemini API key:

   `GEMINI_API_KEY=your_api_key_here`

4. Run the application:

   `streamlit run scholarship_app.py`

## Limitations

- Currently accepts scholarship notice text as input.
- Eligibility results are preliminary guidance and not official scholarship approval.
- Accuracy depends on the information provided in the scholarship notice and student profile.

## Future Enhancements

- PDF and image document upload.
- OCR-based text extraction.
- Support for multiple document formats.
- Improved document analysis and eligibility verification.
