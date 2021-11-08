import pandas as pd
import base64
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
from pycaret.regression import *


st.title('Customer Salary Prediction App')
st.write('')

with st.expander('Focus Prediction'):
    form = st.form(key='my_form')
    age = form.number_input(label='Age', format="%.2f")
    spending_ratio = form.number_input(label='Spending Ratio', format="%.2f")
    annual_spend = form.number_input(label='Annual Spend', format="%.2f")
    gender = form.selectbox(label='Gender', options=['M', 'F'])

    # submit form
    submit_button = form.form_submit_button(label='Submit')

    # show data sumbitted from the form
    if submit_button:
        d = {'age':[int(age)], 'spending_ratio':[spending_ratio],'annual_spend': [annual_spend], 
            'gender':[gender]}
        data = pd.DataFrame(data=d)
        st.write('')
        st.subheader('Customer Data')
        fig =  ff.create_table(data)
        fig.update_layout(width=670)
        st.write(fig)

        st.write('')
        st.write('')
        st.subheader('Predicted Output')

        # make predictions by loading the saved model
        def pred_model(model_name):
            
            model = load_model(model_name)
            
            pred_columns = ['Salary']
            y_pred = model.predict(data)
    
            output_df = pd.DataFrame(y_pred, columns=pred_columns)
            d3 = {'Variable': output_df.columns, 'Predicted Value': output_df.iloc[0]}
            final = pd.DataFrame(data=d3)
            final['Predicted Value'] = int(final['Predicted Value'])
            return final
        
        pred_data = pred_model('salary_model')
        fig =  ff.create_table(pred_data)
        fig.update_layout(width=670)
        st.write(fig)


# section for batch prediction
with st.expander('Batch Prediction'):

    # function to upload the file
    def file_upload(name):
        uploaded_file = st.file_uploader('%s' % (name),key='%s' % (name),accept_multiple_files=False)
        content = False
        if uploaded_file is not None:
            try:
                uploaded_df = pd.read_csv(uploaded_file)
                content = True
                return content, uploaded_df
            except:
                try:
                    uploaded_df = pd.read_excel(uploaded_file)
                    content = True
                    return content, uploaded_df
                except:
                    st.error('Please ensure file is .csv or .xlsx format and/or reupload file')
                    return content, None
        else:
            return content, None

    # function to download resulting predictions
    def download(df,filename): 
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = (f'<a href="data:file/csv;base64,{b64}" download="%s.csv">Download csv file</a>' % (filename))
        return href
    
    # load customer data
    status, df = file_upload('Please upload data to be predicted')

    st.write('')
    st.write('')
    if status:
        st.subheader('Customer Data')
        fig =  ff.create_table(df)
        fig.update_layout(width=670)
        st.write(fig)

    # make predictions on loaded data
    if st.button('Predict'):
        def pred_model(model_name):

            model = load_model(model_name)

            pred_columns = ['Salary']
            
            y_pred = model.predict(df)
            df['predicted_salary'] = y_pred
            return df

        st.write('')
        st.write('')
        st.subheader('Predicted Output')
        pred_data = pred_model('salary_model')
        fig =  ff.create_table(pred_data)
        fig.update_layout(width=670)
        st.write(fig)
        st.markdown(download(pred_data,'Predicted Output'), unsafe_allow_html=True)