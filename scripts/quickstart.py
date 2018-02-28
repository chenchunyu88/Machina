import os

import machina as ma
import pandas as pd

DIR = os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    plans = pd.read_csv(os.path.join(DIR, '../data/medical-plan-2017.csv'))
    client = ma.Client(plans, n_member=1, self_contri=1000, tax_fac=0.25)
    client.fit(300)
    client.plot()
