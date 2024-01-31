
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests 
from time import sleep 
import matplotlib.colors as mpc


class DailySpendPlot():
    ''' timeseries with sales section  '''
    
    # ACCEPTING INPUTS
    def __init__(self, hh_id):
        self.hh_id = hh_id
        #self.data = pd.read_csv('data/hh_summary.csv', index_col=0)

        # actions
    def main(self):
        '''API must be running before this requests.get() call will work.
        fetches the data for self.hh_id from localhost server, and writes it to streamlit'''


        ### class variables
        columns = ["grain_goods"
        ,"seasonal"
        ,"grocery"
        ,"alcohol"
        ,"home_family"
        ,"beverages"
        ,"junk_food"
        ,"concessions"
        ,"kitchen"
        ,"dairy"
        ,"meat"
        ,"drug"
        ,"misc"
        ,"garden"
        ,"produce"
        # ,"total_sales"
        ]
        selected_columns = dict()
        
        ### extract
        res = requests.get(f"http://fastapi-app/hh_daily/{self.hh_id}").json()
        data = pd.DataFrame(res).T

        ## transform
        data = data.set_index('day')
        # hh_key = data['household_key'] # the household identifiers are not contiguous
        data = data.drop(['household_key'], axis=1)


        # mymap = dict(zip(columns, st.columns(len(columns))))
        col1, col2, col3, col4 = st.columns(4)
        for idx, col in enumerate(columns):
            if idx < 4:
                with col1:
                    selected_columns[col] = st.checkbox(f"{col}: ${round(data[col].sum(),2)}", value=True)
            elif idx >= 4 and idx < 8:
                with col2:
                    selected_columns[col] = st.checkbox(f"{col}: ${round(data[col].sum(),2)}", value=True)
            elif idx >= 8 and idx < 12:
                with col3:
                    selected_columns[col] = st.checkbox(f"{col}: ${round(data[col].sum(),2)}", value=True)
            else:
                with col4:
                    selected_columns[col] = st.checkbox(f"{col}: ${round(data[col].sum(),2)}", value=True)


        # selected_columns['total_sales'] = st.checkbox(f"{'total_sales'}: ${round(data['total_sales'].sum(),2)}", value=False) # to show grand total 
        colormap = dict(zip(selected_columns, mpc.XKCD_COLORS.values()))

        st.write(f'# Daily Spend by Section for Household {int(self.hh_id)}') ## NOTE: currently, hh_id is referencing HHSummary['index'] not 'household_key'

        selected = [x for x in selected_columns if selected_columns[x] == True]
        # x = list(data.index)
        # y = np.vstack(data[selected])
        
        fig, ax = plt.subplots()
        # for y in [x for x in selected_columns if selected_columns[x] == True]:
        #     ax.plot(data[y])
        # ax.plot(data[[x for x in selected_columns if selected_columns[x] == True]].sum(axis=1))
        ax.stackplot(data.index, *[data[x] for x in selected], labels=selected, colors=[colormap[x] for x in selected])
        # data[selected].plot.bar(stacked=True, labels=selected, colors=[colormap[x] for x in selected]) # broken
        ax.set_xlabel('Day')
        ax.set_ylabel('Sales')
        fig.legend()

        st.pyplot(fig)
    

if __name__ =='__main__':
    
    import streamlit as st

    def enter_hh_id():
        return int(st.text_input('Enter Household Summary Table Index',value='1'))

 
    a = DailySpendPlot(hh_id=enter_hh_id())
    a.main()
    