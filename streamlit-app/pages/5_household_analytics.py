
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests 
from time import sleep 



class HouseholdAnalytics():
    '''streamlit Implementation class;
    
    simple household-level analytics summary '''
    
    # ACCEPTING INPUTS
    def __init__(self, hh_id):
        self.hh_id = hh_id
        #self.data = pd.read_csv('data/hh_summary.csv', index_col=0)

        # actions
    def main(self):
        '''API must be running before this requests.get() call will work.
        fetches the data for self.hh_id from localhost server, and writes it to streamlit'''
        st.write(f'# Breakdown of Spend for household with index {int(self.hh_id)}') ## NOTE: currently, hh_id is referencing HHSummary['index'] not 'household_key'
        # self.plot_campaign()
        # st.write(self.load_campaign_sales())
        # st.write(self.load_campaign_summary()['Last Day'][self.camp_no])
        # not_running = True
        # while not_running == True:

        #     try:
        res = requests.get(f"http://fastapi-app/hh/{self.hh_id}")
        data = res.json()
        st.write(f'Customer Profile for {self.hh_id}')

        st.write(data)
    
        # table = pd.DataFrame(data=data.values(), index=data.keys())
        # table = table.drop('index', axis=0)
        # table.T.set_index('household_key')


        # st.write(self.data)
        # self.plot_section_sales()
        ## Pie chart, where the slices will be ordered and plotted counter-clockwise:
        ## Section Labels
        # labels = ["alcohol","beverages","concessions","dairy","drug","garden","grain_goods","grocery","home_family","junk_food","kitchen","meat","misc","produce","seasonal"]
        # sizes = [data[x] for x in labels]

        # Plotly Pie Chart
        # fig = px.pie(data, values='pct. of spend', names='Section Label', title=f'Sales By Section for Household {hh_id}')
        # st.plotly_chart(fig)

        # Matplotlib Pie Chart
        # fig1, ax1 = plt.subplots(subplot_kw=dict(aspect="equal"))

        # wedges, texts, formats = ax1.pie(sizes, wedgeprops=dict(width=0.7),startangle=90, 
        #                                   autopct="%1.1f%%", 
        #                                   pctdistance=0.8)
        # # st.write(wedges)
        # kws = dict(arrowprops=dict(arrowstyle="-"),
        #         bbox=dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72),
        #         zorder=0,
        #          va="center")
        # # st.write(formats[0].__dict__)

        # for i, p in enumerate(wedges):
        #     ang = (p.theta2 - p.theta1)/2. + p.theta1
        #     y = np.sin(np.deg2rad(ang))
        #     x = np.cos(np.deg2rad(ang))
        #     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        #     connectionstyle = f"angle,angleA=0.5,angleB={ang}"

        #     kws["arrowprops"].update({"connectionstyle": connectionstyle})
        #     ax1.annotate(f"{labels[i]}", xy=(x, y), 
        #                  xytext=(1.35*np.sign(x), 1.4*y),
        #                 horizontalalignment=horizontalalignment, **kws)
        # st.pyplot(fig1)


        ### show the rest of the data?
        #st.json(data)

                # not_running = False

            # except:
            #     continue
            # finally:
            #     not_Running = True


if __name__ =='__main__':
    
    import streamlit as st

    def enter_hh_id():
        return int(st.text_input('Enter Household Summary Table Index',value='0'))

 
    a = HouseholdAnalytics(hh_id=enter_hh_id())
    a.main()
    