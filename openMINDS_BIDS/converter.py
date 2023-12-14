from bids import BIDSLayout,BIDSValidator
from openminds import core,controlledTerms
from warnings import warn

import json
import os
import pandas as pd
import numpy as np
import datetime

def read_json(file_path: str) -> dict:
  """
  Reads the content of a JSON file and returns it as a Python dictionary.

  Parameters:
  - file_path (str): The path to the JSON file.

  Returns:
  - dict: A Python dictionary containing the content of the JSON file.

  Example:
  >>> data = read_json('example.json')
  >>> print(data)
  {"Name": "The mother of all experiments" , "BIDSVersion": "1.6.0", "DatasetType": "raw" , "License": "CC0" , "Authors": ["Paul Broca" , "Carl Wernicke" ]}
  """
  try:
      # Open the JSON file
      with open(file_path, 'r') as file:
          # Load the JSON content into a dictionary
          json_dic = json.load(file)
      return json_dic
  except FileNotFoundError:
      # Handle file not found error
      print(f"Error: File not found at {file_path}")
      return {}
  except json.JSONDecodeError:
      # Handle JSON decoding error
      print(f"Error: Unable to decode JSON content from {file_path}")
      return {}

def table_filter (dataframe:pd.DataFrame,filter_str:str,column:str="suffix"):
  """
  Filters a Pandas DataFrame based on a specified condition.

  Parameters:
  - dataframe (pd.DataFrame): The DataFrame to be filtered.
  - filter_str (str): The value to filter the DataFrame on.
  - column (str, optional): The column name to apply the filter on. Default is "suffix".

  Returns:
  - pd.DataFrame: A filtered DataFrame containing only the rows that satisfy the condition.
  """
  try:
      # Apply the filter condition on the specified column
      filtered_dataframe = dataframe[dataframe[column] == filter_str]
      return filtered_dataframe
  except KeyError:
      # Handle the case where the specified column is not present in the DataFrame
      KeyError(f"Error: Column '{column}' not found in the DataFrame.")

def unique_items (dataFrame,colume):
    return dataFrame[colume].unique()


def experimental_approach_openminds_create (BIDS_layout_dataFrame):

  experimental_approach_dic={"func":"neuroimaging",
  "dwi":["neuroimaging","neural connectivity"],
  "fmap":"neuroimaging",
  "anat":["neuroimaging","anatomy"],
  "perf":"neuroimaging",
  "meg":"neuroimaging",
  "eeg":"electrophysiology",
  "ieeg":"electrophysiology",
  "beh":"behavior",
  "pet":"radiology",
  "micr":"microscopy",
  "nirs":"neuroimaging"}

  approach_openminds_list=[]
  approach_openminds=[]
  BIDS_approaches=unique_items(BIDS_layout_dataFrame,"datatype")


  for BIDS_approach in BIDS_approaches:
    if not(BIDS_approach==NaN):
      try:
        approach=experimental_approach_dic[BIDS_approach]
      except KeyError:
        warn(f"The {BIDS_approach} is not yet part of openMINDS's acsepted experimental approaches. Please verfy for any typo and check if it is acsepted in BIDS, if it is so please get intouch with openMINDS team for implementing it.")

      if isinstance(approach,list):
      #Detects if there are multiple openMINDs approaches are assosiated with this BIDS Data type
        for approach_delist in approach:
          if not(approach_delist in approach_openminds_list):
            approach_openminds_list.append(approach_delist)
            approach_openminds.append(controlledTerms.ExperimentalApproach.by_name(approach_delist))
      else:
        if not(approach in approach_openminds_list):
          approach_openminds_list.append(approach)
          approach_openminds.append(controlledTerms.ExperimentalApproach.by_name(approach))       

  return approach_openminds
    
def tequnique_openmind(suffix)
  experimental_approach_dic={
    "angio"	:"Angiogram"	,
    "M0map"	:"Equilibrium magnetization (M0) map"	,
    "FLASH"	:"Fast-Low-Angle-Shot image"	,
    "FLAIR"	:"Fluid attenuated inversion recovery image"	,
    "UNIT1" :"Homogeneous (flat) T1-weighted MP2RAGE image"	,
    "inplaneT1"	:"Inplane T1"	,
    "inplaneT2" :"Inplane T2"	,
    "R1map"	:"Longitudinal relaxation rate image"	,
    "T1map"	:"Longitudinal relaxation time image"	,
    "MTVmap":"Macromolecular tissue volume (MTV) image"	,
    "MTRmap":"Magnetization transfer ratio image"	,
    "MTsat"	:"Magnetization transfer saturation image"	,
    "MWFmap":"Myelin water fraction image"	,
    "S0map"	:"Observed signal amplitude (S0) image"	,
    "R2starmap":"Observed transverse relaxation rate image"	,
    "T2starmap":"Observed transverse relaxation time image"	,
    "PDT2"	:"PD and T2 weighted image"	,
    "PDw"	  :"Proton density (PD) weighted image"	,
    "PD"	  :"Proton density image"	,
    "PDmap"	:"Proton density image"	,
    "Chimap":"Quantitative susceptibility map (QSM)"	,
    "RB1map":"RF receive sensitivity map"	,
    "TB1map":"RF transmit field image"	,
    "T1rho"	:"T1 in rotating frame (T1 rho) image"	,
    "T1w"	  :"T1-weighted image"	,
    "T2w"   :"T2-weighted image"	,
    "T2star":"T2* image"	,
    "T2starw":"T2star weighted image"	,
    "R2map"	:"True transverse relaxation rate image"	,
    "T2map"	:"True transverse relaxation time image"	,
    "bold"  : "	Blood-Oxygen-Level Dependent image",
    "cbv"   : "Cerebral blood volume image",
    "phase" : "Phase image",
    "defacemask"  : "Defacing masks",
    "epi"   : "EPI",
    "fieldmap": "Fieldmap",
    "magnitude": "Magnitude",
    "magnitude1": "Magnitude",
    "magnitude2": "Magnitude",
    "phase1": "Phase",
    "phase2": "Phase",
    "phasediff": "Phase-difference",
    "dwi"   : "Diffusion-weighted image",
    "sbref" : "Single-band reference image",
    "asl"   : "Arterial Spin Labeling",
    "m0scan": "M0",
    "eeg"   : "Electroencephalography",
    "ieeg"  : "Intracranial Electroencephalography",
    "physio": "Physiological continuous recordings",
    "stim"  : "stimulation continuous recordings",
    "beh"   : "Behavioral experiments",
    "pet"   : "Positron Emission Tomography",
    "2PE"   : "2-photon excitation microscopy",
    "BF"    : "Bright-field microscopy",
    "CARS"  : "Coherent anti-Stokes Raman spectroscopy",
    "CONF"  : "Confocal microscopy",
    "DIC"   : "Differential interference contrast microscopy",
    "DF"    : "Dark-field microscopy",
    "FLUO"  : "Fluorescence microscopy",
    "MPE"   : "Multi-photon excitation microscopy",
    "NLO"   : "Nonlinear optical microscopy",
    "OCT"   : "Optical coherence tomography",
    "PC"    : "Phase-contrast microscopy",
    "PLI"   : "Polarized-light microscopy",
    "SEM"   : "Scanning electron microscopy",
    "SPIM"  : "Selective plane illumination microscopy",
    "SR"    : "Super-resolution microscopy",
    "TEM"   : "Transmission electron microscopy",
    "uCT"   : "Micro-CT",
    "nirs"  : "Near-Infrared Spectroscopy ",
    "motion": "Motion",
  }
  



def tequniques_openmind_create (BIDS_layout_dataFrame):

  
  approach_openminds_list=[]
  approach_openminds=[]
  BIDS_approaches=unique_items(BIDS_layout_dataFrame,"datatype")

def file_creation ():


def subject_state_creation ():
  

def subject_creation ():




def subjects_creation (subjects_id,layout_df):

  #Find the participants files in the files table
  participants_paths=table_filter(layout_df,'participants')
  #Select the tsv file of the table
  participants_path_tsv=table_filter(participants_paths,'.tsv','extension').iat[0,0]

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
    warn("The Authour section of the BIDS-dataset description file was emphty") 


def dataset_version_create (bids_layout,dataset_description,layout_df):
  
  dataset_version=core.DatasetVersion()

  #Fetch the dataset type from dataset description file 
  if "DatasetType" in dataset_description:
    dataset_type=controlledTerms.SemanticDataType.by_name(dataset_description["DatasetType"])
  
  #Fetch the digitalIdentifier from dataset description file 
  if "DatasetDOI" in dataset_description:
    digital_identifier=core.DOI(
      identifier=dataset_description["DatasetDOI"])

  if "EthicsApprovals" in dataset_description:
    #to be compleated ethics_assessment
    ethics_assessment=controlledTerms.EthicsAssessment.by_name("EU compliant")

  

  #Detect th
  experimental_approach




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
  dataset_description_path=table_filter(layout_df,'description')

  dataset_description=read_json(dataset_description_path.iat[0,0])

  dataset_version=dataset_version_create(bids_layout,dataset_description,layout_df)







