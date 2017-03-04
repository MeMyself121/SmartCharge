import pandas as pd;
import numpy as np;
import datetime;
import math as m;
import scipy.io;
import statsmodels as sm
import statsmodels.tsa.statespace.sarimax as sarima;
import statsmodels.api as sm

if __name__=="__main__":

    raw_data = scipy.io.loadmat("serie.mat")
    #raw_data=np.loadtxt('raw_data.txt')
    #series=raw_data[:,1];
    series = raw_data.get('serie');
    series=series[len(series)-m.floor(len(series)/168)*168:len(series)];
    lnserie=np.log(series);

    d24lnserie = lnserie[24:]-lnserie[0:-24];

    d7d24lnserie = d24lnserie[7:]-d24lnserie[0:-7];

    d1d7d24lnserie = d7d24lnserie[1:]-d7d24lnserie[0:-1];

    #ARIMA Model
    mod = sm.tsa.statespace.SARIMAX(lnserie, trend='n', order=(0, 1, 12), seasonal_order=(0, 1, 1, 168))
    results = mod.fit()


    Mdl = arima('Constant', 0, 'D', 1, 'MALags', [1, 2, 5, 8, 12], 'SMALags', [168], 'Seasonality', 168);
    EstMdl = estimate(Mdl, lnserie)
    [res, V] = infer(EstMdl, lnserie);
    [~, ~, ~, ~, reg] = adftest(res)

    rest1 = 48; % 48
    hours
    rest2 = rest1 - 48;
    tm = rest1 - rest2;

    [yF, yMSE] = forecast(EstMdl, tm, 'Y0', lnserie(1:end - rest1));