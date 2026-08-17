from datetime import date

from dateutil.relativedelta import relativedelta



def calculate_next_maintenance_date(maintenance_date: date) -> date:
    """
    Calculate the next maintenance date.

    The standard maintenance interval is six calendar months.
    """

    return maintenance_date + relativedelta(months=6)