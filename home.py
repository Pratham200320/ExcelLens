import streamlit as st

page_bg_img = """
<style> 
[data-testid="stAppViewContainer"]{
background-color: #66b2de;
opacity: 0.8;
background-image: radial-gradient(circle at center center, #181a4f, #66b2de), repeating-radial-gradient(circle at center
 center, #181a4f, #181a4f, 10px, transparent 20px, transparent 10px);
background-blend-mode: multiply;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

title = st.title("Welcome to ExcelLens 📊")

st.subheader("Unleash Insights, Simplify Data, and Track Expenses", divider='rainbow')

st.markdown("""
<style>
.big-font {
    font-size:19px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font"> <b>ExcelLens is your go-to platform for '
            'transforming raw data into meaningful visualizations. Whether you’re a data enthusiast, '
            'business analyst, or just curious, our app empowers you to:</b></p>', unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Clean Data**: Upload your messy CSV files, and let InsightFlow handle the heavy lifting. Our data cleaning page ensures your data is pristine and ready for analysis.")

with col2:
    st.write("**Visualize with Ease**: Dive into the world of charts, graphs, and interactive plots. Our data visualization page lets you explore trends, correlations, and patterns effortlessly.")

with col3:
    st.write("**Expense Tracker**: Keep your finances in check! Our sunky chart (yes, it’s a sunburst-pie hybrid) provides a delightful overview of your expenses. Track where your money flows and make informed decisions.")

st.markdown("""
    <style>
        [data-testid="column"]{
            background-color: #1c819e;
            border-radius: 10px;
            padding:10px;
            border: 3px solid #ffbe00;
            color: #dfdfdf;
        }
    </style>
    """, unsafe_allow_html=True
)