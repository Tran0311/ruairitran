import os
import numpy as np
import pandas as pd
import NeuroTools.signals as nt

recordings_to_extract = ['CIT_WAY_03_2018-05-07_15-25-21_PRE',
                         'CIT_WAY_03_2018-05-07_16-26-19_cit',
                         'CIT_WAY_03_2018-05-07_17-27-42_way']

kilosort_folder = r'C:\Users\Rory\raw_data\CIT_WAY\dat_files'

spikes_df_csv_out_folder = r'C:\Users\Rory\raw_data\CIT_WAY\spikes_df'
nrn_char_out_fol = r'C:\Users\Rory\raw_data\CIT_WAY\neuron_characteristics'


sampling_rate = 30000

for recording_to_extract in recordings_to_extract:
    print(recording_to_extract)
    path_to_data = '\\'.join([kilosort_folder, recording_to_extract])
    os.chdir(path_to_data)

    out_f1 = '\\'.join([spikes_df_csv_out_folder,
                        recording_to_extract])
    if not os.path.exists(out_f1):
        os.makedirs(out_f1)

    out_f2 = '\\'.join([nrn_char_out_fol,
                        recording_to_extract])
    if not os.path.exists(out_f2):
        os.makedirs(out_f2)

    # load kilosort data files
    print('Loading Data')
    spike_clusters = np.load('spike_clusters.npy')
    spike_times = np.load('spike_times.npy')
    cluster_groups = pd.read_csv('cluster_groups.csv', sep='\t')

    try:  # check data quality
        assert np.shape(spike_times.flatten()) == np.shape(spike_clusters)
    except AssertionError:
        AssertionError('Array lengths do not match in recording {}'.format(
            recording_to_extract))

    # find single unit clusters
    good_clusters_df = cluster_groups.loc[cluster_groups['group'] == 'good', :]
    good_cluster_numbers = good_clusters_df['cluster_id'].values

    # create spikes data frame
    print('Creating Spikes DataFrame')
    labels = ['spike_cluster', 'spike_time']
    data = [spike_clusters.flatten(), spike_times.flatten()]
    data_dict = dict(zip(labels, data))

    df_with_bad_spikes = pd.DataFrame(data)
    df_with_bad_spikes = df_with_bad_spikes.transpose()
    df_with_bad_spikes.rename(columns={0: labels[0], 1: labels[1]},
                              inplace=True)

    # filter only rows corresponding to spikes from single units
    good_spikes_df = df_with_bad_spikes.loc[df_with_bad_spikes['spike_cluster'].isin(
        good_cluster_numbers), :]
    good_spikes_df['time'] = good_spikes_df['spike_time'].divide(sampling_rate)

    # save good spikes df to csv
    good_spikes_df.to_csv('\\'.join([out_f1, recording_to_extract]) + '.csv')

    # extract neuron characteristics
    print('Extracting Neuron Characteristics')
    all_neurons_container = {}
    for cluster in good_cluster_numbers:
        neuron = good_spikes_df.loc[good_spikes_df['spike_cluster'] == cluster]

        spike_times = neuron['time'].values * 1000
        t_start = spike_times[0]
        t_stop = spike_times[-1]
        spike_train_object = nt.SpikeTrain(spike_times,
                                           t_start=t_start,
                                           t_stop=t_stop)

        rate = spike_train_object.mean_rate()
        cv_isi = spike_train_object.cv_isi()

        neuron_dict = {'cluster': cluster, 'rate': rate, 'cv_isi': cv_isi}
        all_neurons_container[cluster] = neuron_dict

    # create and savesave neuron_characteristics_df
    df = pd.DataFrame(data=all_neurons_container)
    df = df.transpose()
    df = df.set_index('cluster')
    print('Saving Neuron Characteristics Dataframe')
    df.to_csv('\\'.join([out_f2, recording_to_extract]) + '.csv')
