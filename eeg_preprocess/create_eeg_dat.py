
# coding: utf-8

import os
from OpenEphys import pack_2


'''

This script converts many .continuous files to one .dat file
It does this with the purpose of creating one .dat file for all the EEG
channels

Change the following parameters:
    openephys_folder = folder containing folders of .continuous files

    recordings_to_pack = list of subfolder names (containing .continuous files)
        within openephys_folder of the recordings you wish to pack

    dat_folder = output folder for the packed .dat file

    chan_map = rearrange channel labels such that channels most physically
        close to each other have consecutive labels
        N.B. only use this if the channel map is not already configured during
        the recordings

NOTE:
    OpenEphys.py must be in the working directory


ROS 2018

'''

# params to change

recordings_to_pack = ['371a_2018-04-11_17-09-39_NO_CNO',
                      '401a_2018-04-18_17-40-36_CNO',
                      'CIT_WAY_1_2018-05-01_15-59-19_PRE',
                      'CIT_WAY_02_2018-05-03_13-38-41_PRE']

openephys_folder = r'C:\Users\Rory\raw_data\CIT_WAY'
dat_folder = r'C:\Users\Rory\raw_data\CIT_WAY\dat_files\eeg'

# for cambridge: linear from top of first shank to bottom of second shank


eeg_chan_nums = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                 46, 47, 48]

chan_map = eeg_chan_nums

ref_method = ''  # 'ave' for common average reference, otherwise chan nums


# pack files

for recording_to_pack in recordings_to_pack:
    print(recording_to_pack)
    raw_data = '\\'.join([openephys_folder, recording_to_pack])
    dat_file_outfolder = '\\'.join([dat_folder, recording_to_pack])
    dat_file_name = '\\'.join([dat_file_outfolder, recording_to_pack]) + '.dat'

    if not os.path.exists(dat_file_outfolder):
        os.makedirs(dat_file_outfolder)

    pack_2(folderpath=raw_data,
           filename=dat_file_name,
           channels=chan_map,
           chprefix='CH',
           dref=ref_method,
           session='0',
           source='100')
