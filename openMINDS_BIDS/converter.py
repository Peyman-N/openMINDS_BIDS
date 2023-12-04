from bids import BIDSLayout,BIDSValidator
from openminds import core
from warnings import warn

import os
import pandas as pd
import numpy as np
import datetime

def file





def subject_creation (subjects_id,layout_dump):

  participants_paths=layout_dump[layout_dump['suffix']=='participants']
  participants_path_tsv=participants_paths[participants_paths['extension']==".json"].iat[0,0]

  participants_table=pd.read_csv(participants_path_tsv, sep='\t', header=0)





  return subject

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


def dataset_version_create (BIDSLayout):
  dataset_version=core.DatasetVersion()
    

  return dataset_version

def dataset_create ():
  
  return dataset

def convert(bids_dir, openminds_dir):
  
  if not(os.path.isdir(bids_dir)):
    raise NotADirectoryError(f"The input directory is not valid, you have specified {bids_dir} which is not a directory.")
  
  if not(BIDSValidator().is_bids(bids_dir)):
    raise NotADirectoryError(f"The input directory is not valid, you have specified {bids_dir} which is not a BIDS directory.")
