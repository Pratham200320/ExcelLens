import streamlit as st
import plotly_express as px
import pandas as pd
import calendar
from datetime import datetime
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="Data Visualization")

# CSS part
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

# Navigation menu
menu = option_menu(
    menu_title=None,
    options=["Home","Data Cleaning","Data Visualization","Expense Register"],
    orientation="vertical",
)

# Home
if menu == "Home":
    st.title("Welcome to ExcelLens 📊")
    st.subheader("Unleash Insights, Simplify Data, and Track Expenses", divider='rainbow')
    st.markdown("""
    <style>
    .big-font {
        font-size:19px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font"> <b>ExcelLens is your go-to platform for'
                'transforming raw data into meaningful visualizations. Whether you’re a data enthusiast, '
                'business analyst, or just curious, our app empowers you to:</b></p>', unsafe_allow_html=True)
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Clean Data: Upload your messy CSV files, and let InsightFlow handle the heavy lifting. Our data cleaning page ensures your data is pristine and ready for analysis.")
    with col2:
        st.write("Visualize with Ease: Dive into the world of charts, graphs, and interactive plots. Our data visualization page lets you explore trends, correlations, and patterns effortlessly.")
    with col3:
        st.write("Expense Tracker: Keep your finances in check! Our sunky chart (yes, it’s a sunburst-pie hybrid) provides a delightful overview of your expenses. Track where your money flows and make informed decisions.")
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
        """, unsafe_allow_html=True)
    # Try to load the GIF; if missing, skip without error
    try:
        if os.path.exists('gif.gif'):
            st.image('gif.gif')
    except:
        pass

# Data Cleaning
if menu == "Data Cleaning":
    st.title("Data Cleaning")
    st.sidebar.subheader("Cleaning Settings")
    uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file", type=['csv', 'xlsx'])
    df = None
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except pd.errors.ParserError:
            df = pd.read_excel(uploaded_file)
        st.subheader("Original Data (Before Cleaning)")
        st.write(df)
        cleaning_select = st.sidebar.selectbox(
            label="Select the Cleaning Type",
            options=['Remove duplicates', 'Drop Column']
        )
        if cleaning_select == 'Remove duplicates':
            df.drop_duplicates(inplace=True)
            st.subheader("Cleaned Data (After Removing Duplicates)")
            st.write(df)
    else:
        st.warning("Please upload a file first !")

# Data Visualization
if menu == "Data Visualization":
    st.title("Data Visualization")
    st.sidebar.subheader("Visualization Settings")
    uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception:
            df = pd.read_excel(uploaded_file)
        st.write(df)
        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    else:
        st.warning("Please upload a file first !")
        numeric_columns = []

    chart = st.sidebar.selectbox(
        label="Select chart type",
        options=['Scatterplot', 'Histogram', 'Pie', 'Line', 'Bar']
    )

    if uploaded_file is not None:
        if chart == 'Scatterplot':
            st.sidebar.subheader("Scatterplot Settings")
            x_value = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_value = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.scatter(data_frame=df, x=x_value, y=y_value)
            st.plotly_chart(plot)
        if chart == 'Histogram':
            st.sidebar.subheader("Histogram Settings")
            x_value = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_value = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_value, y=y_value)
            st.plotly_chart(plot)
        if chart == 'Pie':
            st.sidebar.subheader("Pie Chart Settings")
            names_value = st.sidebar.selectbox('Names', options=numeric_columns)
            values_value = st.sidebar.selectbox('Values', options=numeric_columns)
            plot = px.pie(data_frame=df, names=names_value, values=values_value)
            st.plotly_chart(plot)
        if chart == 'Line':
            st.sidebar.subheader("Line Settings")
            x_value = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_value = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.line(data_frame=df, x=x_value, y=y_value)
            st.plotly_chart(plot)
        if chart == 'Bar':
            st.sidebar.subheader("Bar Settings")
            x_value = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_value = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.bar(data_frame=df, x=x_value, y=y_value, orientation='v')
            st.plotly_chart(plot)

# Expense Register
# Expense Register
if menu == "Expense Register":
    # -------------------SETTINGS---------------
    incomes_list = ["Salary", "Stock", "Other Income"]
    expenses_list = ["Rent", "utilities", "Groceries", "Car", "Other Expenses"]
    currency = "INR"

    # ----DROP DOWN VALUES FOR SELECTING THE PERIOD -----
    years = [datetime.today().year, datetime.today().year + 1]
    months = list(calendar.month_name[1:])

    # Initialize session state for storing expense data
    if 'expense_data' not in st.session_state:
        st.session_state.expense_data = {}

    # --------hide style------------
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility:hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # ---------NAVIGATION MENU------------
    selected = option_menu(
        menu_title=None,
        options=["Data Entry", "Data Visualization", "View All Records"],
        icons=["pencil-fill", "bar-chart-fill", "table"],
        orientation="horizontal"
    )

    # -------------- INPUT AND SAVE PERIODS -------------
    if selected == "Data Entry":
        st.header(f"Data Entry in {currency}")
        
        with st.form("entry_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            selected_month = col1.selectbox("Select Month:", months, key="month")
            selected_year = col2.selectbox("Select Year:", years, key="year")

            "---"
            with st.expander("Income", expanded=True):
                income_values = {}
                for income_item in incomes_list:
                    income_values[income_item] = st.number_input(f"{income_item}:", min_value=0, format="%i", step=1000, key=f"input_{income_item}")
            
            with st.expander("Expense", expanded=True):
                expense_values = {}
                for expense_item in expenses_list:
                    expense_values[expense_item] = st.number_input(f"{expense_item}:", min_value=0, format="%i", step=100, key=f"input_{expense_item}")
            
            with st.expander("Comment"):
                comment = st.text_area("", placeholder="Enter your comment here...", key="comment_input")

            "---"

            submitted = st.form_submit_button("💾 Save Data")
            if submitted:
                period = f"{selected_year}_{selected_month}"
                
                # Store data in session state
                st.session_state.expense_data[period] = {
                    'incomes': income_values.copy(),
                    'expenses': expense_values.copy(),
                    'comment': comment,
                    'total_income': sum(income_values.values()),
                    'total_expense': sum(expense_values.values()),
                    'savings': sum(income_values.values()) - sum(expense_values.values()),
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Display summary
                st.success(f"✅ Data saved successfully for {period}!")
                st.balloons()
                
                col1, col2, col3 = st.columns(3)
                col1.metric("💰 Total Income", f"₹{sum(income_values.values()):,}")
                col2.metric("💸 Total Expense", f"₹{sum(expense_values.values()):,}")
                col3.metric("💵 Savings", f"₹{sum(income_values.values()) - sum(expense_values.values()):,}")

    # ----------------PLOT PERIODS------------------
    elif selected == "Data Visualization":
        st.header("📊 Data Visualization")
        
        if not st.session_state.expense_data:
            st.warning("⚠️ No data available! Please enter some data first.")
        else:
            # Let user select from saved periods
            available_periods = list(st.session_state.expense_data.keys())
            selected_period = st.selectbox("📅 Select Period:", ["Select a period..."] + available_periods)
            
            if selected_period != "Select a period...":
                data = st.session_state.expense_data[selected_period]
                
                # Display metrics
                col1, col2, col3 = st.columns(3)
                col1.metric("💰 Total Income", f"₹{data['total_income']:,}")
                col2.metric("💸 Total Expense", f"₹{data['total_expense']:,}")
                col3.metric("💵 Savings", f"₹{data['savings']:,}")
                
                if data['comment']:
                    st.info(f"💭 Comment: {data['comment']}")
                
                # Create Sankey chart
                st.subheader("💹 Cash Flow Visualization")
                
                # Filter out zero values for cleaner visualization
                filtered_incomes = {k: v for k, v in data['incomes'].items() if v > 0}
                filtered_expenses = {k: v for k, v in data['expenses'].items() if v > 0}
                
                if filtered_incomes and filtered_expenses:
                    # Create labels for Sankey
                    labels = list(filtered_incomes.keys()) + ["Total Income"] + list(filtered_expenses.keys())
                    
                    # Create source and target arrays
                    source = list(range(len(filtered_incomes))) + [len(filtered_incomes)] * len(filtered_expenses)
                    target = [len(filtered_incomes)] * len(filtered_incomes) + [labels.index(k) for k in filtered_expenses.keys()]
                    values = list(filtered_incomes.values()) + list(filtered_expenses.values())
                    
                    # Create Sankey diagram
                    link = dict(source=source, target=target, value=values)
                    node = dict(label=labels, pad=20, thickness=30, 
                               color=["lightblue"]*len(filtered_incomes) + ["orange"] + ["lightcoral"]*len(filtered_expenses))
                    
                    sankey = go.Sankey(link=link, node=node)
                    fig = go.Figure(sankey)
                    fig.update_layout(
                        title=f"Cash Flow for {selected_period}",
                        font_size=12,
                        margin=dict(l=0, r=0, t=50, b=10)
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Show breakdown
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("💰 Income Breakdown")
                        income_df = pd.DataFrame(list(filtered_incomes.items()), columns=['Source', 'Amount'])
                        st.dataframe(income_df, use_container_width=True)
                    
                    with col2:
                        st.subheader("💸 Expense Breakdown")
                        expense_df = pd.DataFrame(list(filtered_expenses.items()), columns=['Category', 'Amount'])
                        st.dataframe(expense_df, use_container_width=True)
                else:
                    st.warning("⚠️ No income or expense data to visualize for this period.")

    # ----------------VIEW ALL RECORDS------------------
    elif selected == "View All Records":
        st.header("📋 All Expense Records")
        
        if not st.session_state.expense_data:
            st.warning("⚠️ No records found! Please add some data first.")
        else:
            # Summary statistics
            total_periods = len(st.session_state.expense_data)
            total_income_all = sum([data['total_income'] for data in st.session_state.expense_data.values()])
            total_expense_all = sum([data['total_expense'] for data in st.session_state.expense_data.values()])
            total_savings_all = total_income_all - total_expense_all
            
            st.subheader("📈 Overall Summary")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("📅 Total Periods", total_periods)
            col2.metric("💰 Total Income", f"₹{total_income_all:,}")
            col3.metric("💸 Total Expenses", f"₹{total_expense_all:,}")
            col4.metric("💵 Net Savings", f"₹{total_savings_all:,}")
            
            # Display all records in a table
            st.subheader("📊 Detailed Records")
            records_data = []
            for period, data in st.session_state.expense_data.items():
                records_data.append({
                    'Period': period,
                    'Total Income': f"₹{data['total_income']:,}",
                    'Total Expense': f"₹{data['total_expense']:,}",
                    'Savings': f"₹{data['savings']:,}",
                    'Comment': data['comment'] if data['comment'] else 'No comment',
                    'Saved On': data['timestamp']
                })
            
            records_df = pd.DataFrame(records_data)
            st.dataframe(records_df, use_container_width=True)
            
            # Option to clear all data
            st.subheader("🗑️ Data Management")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🗑️ Clear All Data", type="secondary"):
                    st.session_state.expense_data = {}
                    st.rerun()
            
            with col2:
                # Export data as JSON (simplified)
                if st.button("📥 Download Data", type="secondary"):
                    import json
                    json_str = json.dumps(st.session_state.expense_data, indent=2)
                    st.download_button(
                        label="📄 Download JSON",
                        data=json_str,
                        file_name=f"expense_data_{datetime.now().strftime('%Y%m%d')}.json",
                        mime="application/json"
                    )
