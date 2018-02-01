import os
import pandas as pd

type_col = 'Which of the following best characterizes your form of MS? (MSbestcharacterizes)'
types = ['CIS', 'rrms', 'spms', 'ppms', '99']

#Setting Up Template
fields  = ['Owner ID', type_col]
temp_df = pd.read_csv(os.getcwd()+'/data/report_Clinical_History_-_Diagnostic_Details_b80360d8_2018.01.09.csv', skipinitialspace=True, usecols=fields)
temp_df.set_index('Owner ID', inplace = True)


#Creates a new dataframe using the template
def create_df (files, temp_df):
    for f in files:
        data = pd.read_csv(f)
        data.set_index('Owner ID', inplace =True)
        temp_df = pd.concat([temp_df,data], axis=1)
    return temp_df

# '''function to show percentages in crosstable'''
def percConvert(ser):
  return ser/float(ser[-1])

#functino to create a new data frame with the types of MS
def new_df():
    d = {'type': ['CIS', 'rrms', 'spms', 'ppms', '99']}
    data = pd.DataFrame(data=d)
    data.set_index('type', inplace=True)
    return data

#function to create cross table with percentages
def create_crosstab(a,b, df):
    table = pd.crosstab(df[b],df[a],margins=True, normalize = 'columns' )
    return table


#Symptoms Visualization

sym_df = create_df(['/Users/navilcoding/visualization/data/report_Clinical_History_-_Symptoms_b264356d_2018.01.09.csv'], temp_df)

sym_1 = ['[symptoms1]:Weakness in arms/hands (Weaknessarms)','[symptoms1]:Weakness in legs/feet (Weaknesslegs1)','[symptoms1]:Difficulty walking / dragging a foot (Difficultywalking1)','[symptoms1]:Loss of coordination in arms / hands (Losscoordinationarm1)', '[symptoms1]:Loss of coordination in legs / feet (Losscoordinationleg)','[symptoms1]:Stiffness / spasms (Stiffness1)','[symptoms1]:Difficulty with balance (Difficulybalance)',	'[symptoms1]:Shaking or tremors (Shaking1)']
sym_2 = ['[symptoms2]:Paralysis of half or whole face (i.e. facial drooping with altered smile, difficulty closing an eye tightly or wrinkling forehead) (Paralysis1)', '[symptoms2]:Facial twitching (FacialTwitching)','[symptoms2]:Speech articulation (speech sounds slurred or slowed or loses normal rhythm) (SpeechArticulation)','[symptoms2]:Difficulty with swallowing (Difficultyswallowing1)','[symptoms2]:Blindness or blurry vision in one eye or both (Blindness1)','[symptoms2]:Disturbed vision e.g. double vision, objects moving, etc. (Disturbedvision)', '[symptoms2]:Sensory symptoms: Loss of feeling, painful feeling, unable to feel position of fingers/arms/legs, swollen feeling, numbness, tingling, feeling of pinpricks (Sensory11)', '[symptoms2]:Painful sensations (Sensory11Pain)', '[symptoms2]:Sensory symptoms (excluding pain): Loss of feeling, unable to feel position of fingers/arms/legs, swollen feeling, numbness, tingling, feeling of pinpricks (Sensory11_NoPain)']
sym_3 = ['[symptoms3]:Vertigo (Vertigo1)','[symptoms3]:Sharp, painful feeling in face not due to trauma or injury (trigeminal neuralgia) (TrigeminalNeuralgia)','[symptoms3]:Electric shock-like feeling when bending neck (Electricshockfeeling)','[symptoms3]:Itching, not due to other causes e.g. psoriasis, insect bites, etc. (Itching1)','[symptoms3]:Burning sensation in feet (Burningsensationfeet)','[symptoms3]:Cognitive difficulties, e.g. memory problems (CognitiveDifficulties)','[symptoms3]:Sexual dysfunction, not caused by medication (SexualDysfunction)','[symptoms3]:Urinary problems, e.g. unusual urgency or hesitancy (UrinaryProblems)']
sym_4 = ['[symptoms4]:Trouble with bowel movements (Troublebowelmovements1)', '[symptoms4]:Fatigue (Fatigue2)', '[symptoms4]:Changes in mood or depression considered out of the ordinary (Depression)', '[symptoms4]:Total paralysis of legs (Legstotalparalysis)', '[symptoms4]:Total paralysis of arms (Armstotalparalysis)', '[symptoms4]:Need for mechanical ventilation (MechanicalVentilation)', '[symptoms4]:"MS hug" (feeling of tightness in the torso) (MShug)', '[symptoms4]:Restless leg syndrome (RestlessLeg)']

label_dict = pd.read_csv(os.getcwd()+'/labels.csv',skipinitialspace=True)
label_dict.set_index('symptom', inplace =True)

symptoms = [sym_1, sym_2, sym_3, sym_4]
sym_export = []

for sym_type in symptoms:

    #created a empty df to convert to csv
    sym_csv = pd.DataFrame()
    sym_csv['group'] = None
    sym_csv['axis'] = None
    sym_csv['value'] = 0.0
    sym_csv['description'] = None
    count = 0

    for sym in sym_type:

        #getting frequency values
        for x in sym_df.index:
            if '4' in str(sym_df[sym][x]) or '5' in str(sym_df[sym][x]):
                sym_df.at[x, sym]= 'no'
            else:
                sym_df.at[x, sym] = 'yes'

        #create cross table
        sym_1_ct = create_crosstab(type_col, sym, sym_df)

        #add data
        for t in types:
            count +=1
            label = label_dict.at[sym, 'label']
            print(label)
            type_label = label_dict.at[t, 'label']

            val = sym_1_ct[t]['yes']*100
            add = [type_label, label, val, sym]

            sym_csv.loc[count] = add
            # print (sym_csv)

    sym_export.append(sym_csv)



sym_export[0].to_csv('sym1.csv')
sym_export[1].to_csv('sym2.csv')
sym_export[2].to_csv('sym3.csv')
sym_export[3].to_csv('sym4.csv')
