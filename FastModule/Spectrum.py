def read_wav_file(Path):
    #Path is an string
    import thinkdsp
    return thinkdsp.read_wave(Path)

def plot_spectrum(wavefile):
    #sent wave array not path
    spectruminplt=wavefile.make_spectrum()
    spectruminplt.plot()
    
def make_amplitude_per_frequency_DataFrame(wavefile):
    #from __future__ import print_function, division
    import thinkdsp
    import thinkplot
    import pandas as pd
    import numpy as np
    from pandas import DataFrame
    from sklearn.preprocessing import MinMaxScaler
    
    spectruminmas=wavefile.make_spectrum()
    
    scaler = MinMaxScaler()
    
    dataf=pd.DataFrame()
    dataf['Frequency']=spectruminmas.fs
    dataf['Amplitude']=np.abs(spectruminmas.hs)
    dataf['Normalized']=scaler.fit_transform((np.abs(spectruminmas.hs)).reshape(-1,1))
    dataf.set_index('Frequency',inplace=True)
    return dataf

def make_csv_file(inputDataFrame,Filename="Test_output"):
    import pandas as pd
    from pandas import DataFrame
    Filename="."+"/"+"output"+"/"+Filename+"."+"csv"
    inputDataFrame.to_csv(Filename)
    return Filename