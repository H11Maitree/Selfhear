def caculate_trasmission(datain,dataout,colum='Amplitude'):
    from pandas import DataFrame
    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    
    scaler = MinMaxScaler()
        
    dataf=pd.DataFrame()
    dataf['Frequency']=datain.index
    dataf['Percent_out_per_in']=np.array(dataout[colum])/np.array(datain[colum])
    dataf['Normalized_Percent']=scaler.fit_transform((np.array(dataf.Percent_out_per_in)).reshape(-1,1))
    dataf['Normalized_Percent_loss']=1-dataf['Normalized_Percent']
    dataf.set_index('Frequency',inplace=True)
    return dataf