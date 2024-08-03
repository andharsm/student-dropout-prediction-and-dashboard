import streamlit as st
import json
import joblib
import numpy as np

mapping = './model/mapping.json'

# Membaca file JSON
with open(mapping, 'r') as file:
    data = json.load(file)

# Memuat model dari file joblib
model = joblib.load('./model/model_rf_fitur_2.joblib')

# Mengakses bagian mapping
course_mapping = data.get("course_mapping", {})
scholarship_mapping = data.get("scholarship_holder_mapping", {})
tuition_fees_mapping = data.get("tuition_fees_up_to_date_mapping", {})

# Mendapatkan daftar nilai dari mapping
course_list = list(course_mapping.values())
scholarship_list = list(scholarship_mapping.values())
tuition_fees_list = list(tuition_fees_mapping.values())

def get_key_from_value(mapping, value):
    """Mengambil kunci berdasarkan nilai dari sebuah mapping."""
    for key, val in mapping.items():
        if val == value:
            return key
    return None 

def main():
    st.title("Student Dropout Prediction")

    st.header("Registration and Background Information", divider='grey')

    col1, col2 = st.columns(2)

    with col1:
        course = st.selectbox("Course", ["select an option"] + course_list)
        previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=90.0, max_value=190.0, step=0.1, format="%.1f")

    with col2:
        age_at_enrollment = st.number_input("Age", min_value=16, max_value=100, step=1, format="%d", help="Enter your age in years")
        admission_grade = st.number_input("Admission Grade", min_value=90.0, max_value=190.0, step=0.1, format="%.1f")

    st.header("Financial Status", divider='grey')
    scholarship = st.selectbox("Scholarship", ["select an option"] + scholarship_list)
    tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", ["select an option"] + tuition_fees_list)

    st.header("Academic Performance", divider='grey')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1st Semester")
        curricular_units_1st_sem_evaluations = st.slider("Curricular Units 1st Semester Evaluations", min_value=0, max_value=45, value=5)
        curricular_units_1st_sem_approved = st.slider("Curricular Units 1st Semester Approved", min_value=0, max_value=45, value=5)
        curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Semester Grade", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")

    with col2:
        st.subheader("2nd Semester")
        curricular_units_2nd_sem_evaluations = st.slider("Curricular Units 2nd Semester Evaluations", min_value=0, max_value=45, value=5)
        curricular_units_2nd_sem_approved = st.slider("Curricular Units 2nd Semester Approved", min_value=0, max_value=45, value=5)
        curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Semester Grade", min_value=0.0, max_value=100.0, step=0.1, format="%.1f")

    # Submit button
    if st.button("Submit"):
        if course == "select an option":
            st.error("You have not selected a course. Please select a course first.")
        elif scholarship == "select an option":
            st.error("You have not selected the scholarship status. Please choose a scholarship option.")
        elif tuition_fees_up_to_date == "select an option":
            st.error("You have not selected the tuition fees status. Please choose the tuition fees status.")
        else:
            course_key = get_key_from_value(course_mapping, course)
            scholarship_key = get_key_from_value(scholarship_mapping, scholarship)
            tuition_fees_key = get_key_from_value(tuition_fees_mapping, tuition_fees_up_to_date)

            data = [course_key,
                    previous_qualification_grade,
                    curricular_units_1st_sem_evaluations,
                    scholarship_key,
                    admission_grade,
                    age_at_enrollment,
                    curricular_units_2nd_sem_evaluations,
                    tuition_fees_key,
                    curricular_units_1st_sem_grade,
                    curricular_units_1st_sem_approved,
                    curricular_units_2nd_sem_grade,
                    curricular_units_2nd_sem_approved
                    ]

            print(data)

            # Ubah data menjadi array 2D
            data_array = np.array(data).reshape(1, -1)

            pred = model.predict(data_array)

            if pred == 0:
                label = 'Graduate'
            else:
                label = 'Dropout'

            st.success(f"The predicted result from the data you input is **{label}**")

    else:
        st.info("Please complete the form above before submitting.")

if __name__ == '__main__':
    main()
