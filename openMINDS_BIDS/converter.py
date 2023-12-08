from bids import BIDSLayout,BIDSValidator
from openminds import core,controlledTerms
from warnings import warn

import json
import os
import pandas as pd
import numpy as np
import datetime

def tequniques_openmind (teqnique_BIDS):


def file_creation ():


def subject_state_creation ():
  

def subject_creation ():




def subjects_creation (subjects_id,layout_df):


  participants_paths=layout_df[layout_df['suffix']=='participants']

  participants_path_tsv=participants_paths[participants_paths['extension']==".tsv"].iat[0,0]

  participants_table=pd.read_csv(participants_path_tsv, sep='\t', header=0)

  for 






  return subjects

def person_create(persons_list):

  if isinstance(persons_list,list):
    persons=[]
    for author in persons_list:
        names=author.split()
        last_name=names[-1]
        first_name=" ".join(names[:-1])
        new_person=core.Person(
            family_name=last_name,
            given_name=first_name
          )
        persons.append(new_person)
    return persons
  elif isinstance(persons_list,str):
    names=persons_list.split()
    last_name=names[-1]
    first_name=" ".join(names[:-1])
    new_person=core.Person(
      family_name=last_name,
      given_name=first_name
      )
    return new_person
  else:
    warn("The Authour section of the BIDS- was ") 


def dataset_version_create (bids_layout,dataset_description,layout_df):
  
  dataset_version=core.DatasetVersion()

  if "DatasetType" in dataset_description:
    dataset_type=SemanticDataType.by_name(dataset_description["DatasetType"])



  #creating a list containig all the Modalities used in this dataset
  suffixs=layout_df['suffix'].unique()
  techniques=tequniques_openmind(suffixs)



    

  return dataset_version



def dataset_create ():
  
  return dataset




def convert(bids_dir, openminds_dir):
  
  if not(os.path.isdir(bids_dir)):
    raise NotADirectoryError(f"The input directory is not valid, you have specified {bids_dir} which is not a directory.")
  
  if not(BIDSValidator().is_bids(bids_dir)):
    raise NotADirectoryError(f"The input directory is not valid, you have specified {bids_dir} which is not a BIDS directory.")
  
  bids_layout=BIDSLayout(bids_dir)

  layout_df=bids_layout.to_df()

  subjects=bids_layout.get_subjects()

  tasks=bids_layout.get_task()

  #imprting the datset description file containing some of the 
  dataset_description_path=layout_df[layout_df['suffix']=='description']
  dataset_description_f=open(dataset_description_path.iat[0,0])
  dataset_description=json.load(dataset_description_f)
  dataset_description_f.close()

  dataset_version=dataset_version_create(bids_layout,dataset_description,layout_df)







