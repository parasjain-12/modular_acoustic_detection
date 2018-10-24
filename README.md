# Modular Acoustic Detection

## Environment Setup

To download all the relevant Ubuntu packages:
```shell
# Make script executable
$ chmod 777 ubuntu_packages_install.sh

# Run script to install
$ ./ubuntu_packages_install.sh
```

## Local repo setup

##### 1. To load all git submodules :

```shell
$ git submodule update --init --recursive
```
<br>

##### 2. To download all the data files :
```shell
# Make script executable
$ chmod 777 download_data_files.sh

$ ./download_data_files.sh
```
<br>

**3. To download all the sound files** : (This is a really lengthy process and hence is not advisable unless you absolutely have to):
```shell
$ python download_all_sounds.py
```
<br>

##### 4. To download only your sounds of Interest : 


This will download the sounds ( _.wav files_ ) that you are interested in, from enlisted sounds of  [Google audioset](https://research.google.com/audioset/). you can see the list for class of sounds by using ```[-h]``` argument for script in command line .

```
$ python download_soi.py [-h] [-target_sounds TARGET_SOUNDS] [-target_path TARGET_PATH]

```
###### Output of the above script will return:
- Creates a base dataframe file with name ```downloaded_base_dataframe.pkl``` having details like ```[ YTID, start_seconds, end_seconds, positive_labels, labels_name, wav_file ]``` of each audio file.
- Downloads all the target sounds

<br>

##### 5. To generate the embeddings for the downloaded audio files :

This will download the embeddings in ```.pkl``` files at the directory where you specify. This script requires additional functional scripts found at [Tensorflow-models-repo](https://github.com/tensorflow/models/tree/9b57f41ce21cd7264c52140c9ab31cdfc5169fcd/research/audioset).

```shell
$ python generating_embeddings.py --wav_file /path/to/a/wav/file \
                                    --tfrecord_file /path/to/tfrecord/file \
                                    --checkpoint /path/to/model/checkpoint \
                                    --pca_params /path/to/pca/params \
				    --path_to_write_embeddings /path/to/write/embeddings
```
###### Output of above script will return :
- embeddings in ```.pkl``` files for each downloaded audio file at specified directory. 

<br>

##### 6. To add generated embeddings of each audio file to _base dataframe_ :
This will add the generated embedding values of each audio file to base dataframe columns. Final dataframe will now have one extra column when compared with ```downloaded_base_dataframe.pkl``` ie with ```[features]```
```shell
$ python add_embeddings_to_base_df.py [-h] [-path_to_embeddings PATH_WHERE_EMBEDDINGS_SAVED]
```
###### Output of this script will return :
- ```downloaded_final_dataframe.pkl``` file is generated with columns ```[YTID, start_seconds, end_seconds, positive_labels, labels_name, wav_file, features]``` ie ```[features]``` column is added to base dataframe 

<br>

##### 7. To separate out the different sounds based on labeling :
This script will read the ```downloaded_final_dataframe.pkl``` generated from ```add_embeddings_to_base_df.py``` and separates out the sounds based on labeling. You can check [coarse_labels.csv](https://github.com/wildlytech/modular_acoustic_detection/blob/master/coarse_labels.csv) file to know the mapping of the labels and the separation of each sounds takes place. 

```
$ python seperating_different_sounds.py [-h] [-path_to_write_different_sounds PATH_TO_WRITE_DIFFERENT_SOUNDS ]
```
###### Output of this script return :
- Dataframes with type of sound and number of examples of that sound as name of file in specified path directory.

<br>

##### 8. To Balance the data :
This script reads all the dataframes that are generated by running ```seperating_different_sounds.py``` and concats all the dataframes and balances the percentages of each sound examples .

```
$ python balancing_dataset.py
```
###### output returns :
- Dataframe with equal percentage of different sounds.

<br>

##### 9. To train the Binary model :
This is will call the ```balancing_dataset.py``` function to get the balanced dataframe for training the binary model. It detects anomaly as ```Impact sounds``` and non-anomaly as ```Ambinet sounds```. Impact sounds are given ```1``` 's and Ambient sounds as ```0```'s. 
```
$ python binary_model.py [-h] [-save_weights SAVE_WEIGHTS]
```
###### output returns:
- ```.h5```  file is saved consists of weights of the trained ```binary_model.py```

<br>

##### 10. To train a Multi-label model :
This will call ```balancing_dataset.py``` function to get the balanced dataframe for training the multi-label model. 
```
$ python multilabel_model.py [-h] [-save_weights SAVE_WEIGHTS] 
```

###### output returns:

- ```.h5``` file is saved consists of weights of the trained ```multiclass_model.py```



