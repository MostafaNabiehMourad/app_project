import streamlit as st
import pandas as pd

superSales = pd.read_csv('superSales.csv')

st.set_page_config(page_title='Super Sales Dashboard'
                   , page_icon='https://static.vecteezy.com/system/resources/previews/014/809/566/original/data-analyst-line-icon-vector.jpg')


st.markdown(
    """
    <style>
    .top-stats {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 12px 0 40px 0;
        width: 100%;
        height: 40px;
    }
    .subheader {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stat {
        flex: 1; 

        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        background-color: #111;

        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .stat p {
        padding-top: 8px;
    }
    .stat p {
        color: #bbb;
        font-size: 12px;
    }
    .stat span {
        color: #ddd;
        font-size: 24px;
        font-family: serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)




home = st.container()

topRow = st.container()

MidRow = st.container()

chartRow = st.container()

# Done
footer = st.container()

with st.sidebar:
    st.title(" About the dataset")
    st.markdown('Super market dataset ')
    Product_lines = superSales['Product_line'].unique()
    line = st.selectbox('',['Choose the product line']+list(Product_lines))
    if line == 'Choose the product line':
        choses_line = superSales
    else:
        choses_line = superSales[superSales['Product_line'] == line]
with home: 
    st.image('https://media.istockphoto.com/id/1257312690/vector/analytics-bar-graph-icon.jpg?s=612x612&w=0&k=20&c=3u12q178en00xfxgjwz3xRaTGwrGmWFRdDc3HbJOGHw=')
    st.title("Super Selas")
    st.markdown('## the demo project')
    
with topRow:
    total_invoices = choses_line.shape[0]
    average_rateing = choses_line['Rating'].mean()
    most_active = choses_line['Order_time'].mode()[0]
    st.markdown(
        """
        <div class="subheader">Top Stats</div>
        <div class="top-stats">
            <div class="stat">
                <p>Total Invoices<br><span> %d </span></p>
            </div>
            <div class="stat">
                <p>Average Rating<br><span> %.2f </span></p>
            </div>
            <div class="stat">
                <p>Most Active Time<br><span> %s </span></p>
            </div>
        </div>
        """ % (total_invoices, average_rateing, most_active),
        unsafe_allow_html=True
    )
    
    
with MidRow:
    income = choses_line['Total_price'].sum()
    cost  = choses_line['costs'].sum()
    profit = income - cost 
    st.markdown(
        """
        <div class="subheader">Top Stats</div>
        <div class="top-stats">
            <div class="stat">
                <p>income Total<br><span> %d </span></p>
            </div>
            <div class="stat">
                <p>cost Total<br><span> %.2f </span></p>
            </div>
            <div class="stat">
                <p>profit Total<br><span> %s </span></p>
            </div>
        </div>
        """ % (income, cost, profit),
        unsafe_allow_html=True
    )
    
    
with chartRow:
    superSales['Order_date'] = pd.to_datetime(superSales['Order_date'])
    month  = superSales['Order_date'].dt.month == 1
    data = choses_line[month]
    total_quantity = data.groupby('Order_date')['Quantity'].sum()
    st.line_chart(total_quantity)
    
    
    

with footer:
    st.markdown('---')
    st.markdown(
        """
        <style>
            p {
                font-size: 16px;
                text-align: center;
            }
            a {
                text-decoration: none;
                color: #00a;
                font-weight: 600;
            }
        </style>
        <p>
        Mostafa Nabieh

        </p>
        
        """,
        unsafe_allow_html=True
        )