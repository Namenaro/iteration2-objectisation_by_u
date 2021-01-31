
import os
import easygui
import json

PATH_TO_METADATASETS_FOLDER =  "C:\\mywork\\revive_gobby\\dataset_instanses"

def load_json(file_path=None):
    text = "select json"
    if file_path is None:
        file_path = easygui.fileopenbox(text)
        if file_path is None:
            return None
    with open(file_path, 'r') as f:
        return json.load(f)

def get_7_helthy_json():
    file_path = os.path.join(PATH_TO_METADATASETS_FOLDER, "7_pacients_ideally_healthy_and_normal_axis.json")
    json_data = load_json(file_path)
    return json_data

def get_lead_signal(ecg_json, lead_name):
    return ecg_json['Leads'][lead_name]['Signal']

def get_ecg_description(ecg_json):
    return ecg_json["TextDiagnosisDoc"]

def get_points(json_node, component, n_in_triple):
    triplets = json_node['Leads']['i']['DelineationDoc'][component]
    res = list([t[n_in_triple] for t in triplets])
    return res

