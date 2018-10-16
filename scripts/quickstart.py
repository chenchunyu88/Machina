import os

import machina
import pandas as pd

DIR = os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    plans = pd.read_csv(os.path.join(DIR, '../data/medical-plan-2018.csv'))
    client = machina.Engine(plans, n_member=2, self_contri=1000, tax_fac=0.15)
    client.fit(iter=400)
    client.plot()
