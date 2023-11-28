import streamlit as st

# Route to home page
def index():
    st.title('Student Performance Analyze')
    st.write('Please fill in the following details:')
    gender = st.selectbox('Gender', ['male', 'female'])
    race_ethnicity = st.selectbox('Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
    parental_education = st.selectbox('Parental Education', ['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"])
    lunch = st.selectbox('Lunch Type', ['standard', 'free/reduced'])
    test_prep = st.selectbox('Test Preparation Course', ['none', 'completed'])
    reading_score = st.number_input('english ', min_value=0, max_value=100)
    writing_score = st.number_input('Writing Score', min_value=0, max_value=100)
    
    if st.button('Analyze'):
        
        average = (reading_score+writing_score)/2
        y = (0.94066*average) + 12.17384
        results = y
        
        if results >= 100 or results >= 90:
            st.success('Results: 100')
            st.write('Keep up the good work!')
        elif results <= 90 and results >= 70:
            st.success(f'Results: {results}')
            st.write('Good work!')
        elif results <= 70 and results >= 35:
            st.warning(f'Results: {results}')
            st.write('You must work hard.')
        elif results < 35:
            st.error(f'Results: {results}')
            st.write('You failed.')
        else:
            st.write(f'Results: {results}')

if __name__ == '__main__':
    index()
