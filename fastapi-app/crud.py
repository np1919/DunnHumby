from sqlalchemy.orm import Session

import models, schemas

def get_hh(hh_id:int
            ,db: Session):
    '''return the customer profile for 
    INDEX == hh_id.'''
    return db.query(models.HHSummary).filter(models.HHSummary.index == hh_id).first()


def get_daily_campaign_sales(camp_id:int
                             ,db:Session):
    '''return the daily sales table for `camp_id`'''
    data_in = db.query(models.DailyCampaignSales).filter(models.DailyCampaignSales.campaign_id==camp_id).all()

    data_out = dict()
    for x in data_in:
        temp = x.__dict__
        index = temp.pop('index')
        temp.pop('_sa_instance_state')
        temp.pop('campaign_id')
        data_out[index] = temp

        # take only the day and sales values?
#     data_out = {'datetime':[x.datetime for x in data_in],
#                     'sales_value':[x.sales_value for x in data_in]}
    return data_out


def daily_hh_sales(hh_id:int
            ,db: Session):
    '''return the customer profile for 
    INDEX == hh_id.'''
    # return {1:1}
    data_in = db.query(models.DailyHHSpend).filter(models.DailyHHSpend.household_key == hh_id).all()

    data_out = dict()
    for x in data_in:
        temp = x.__dict__
        index = temp.pop('index')
        temp.pop('_sa_instance_state')
        data_out[index] = temp
    return data_out
