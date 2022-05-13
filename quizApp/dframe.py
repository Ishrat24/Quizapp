import pandas as pd
from pathlib import Path

# path = Path("C:/Users/Desktop/CSCI 348/Project/quizApp/database")
path = Path("database")


def count_reset():
    df = pd.read_csv(path / 'participantList.csv')
    df = df[['participant_id', 'Name', 'Gender', 'College', 'City', 'Passw', 'quizTaken']]
    for index, row in df.iterrows():
        df['quizTaken'].iloc[index] = 0
    df.to_csv(path / 'participantList.csv')

    df = pd.read_csv(path / 'options.csv')
    df = df[['Options', 'Name', 'Option Pick Count']]
    for index, row in df.iterrows():
        df['Option Pick Count'].iloc[index] = 0
    df.to_csv(path / 'options.csv')


def reset_options_list():
    df = pd.DataFrame(columns=['participant_id', 'Name', 'Gender', 'College', 'City', 'Passw', 'quizTaken'])
    df = df[['participant_id', 'Name', 'Gender', 'College', 'City', 'Passw', 'quizTaken']]
    df.to_csv(path / 'participantList.csv')


def reset_participant_list():
    df = pd.DataFrame(columns=['Options', 'Name', 'Option Pick Count'])
    df = df[['Options', 'Name', 'Option Pick Count']]
    df.to_csv(path / 'options.csv')


def verifyIdPassword(pid, passw):
    df = pd.read_csv(path / 'participantList.csv')
    df = df[['participant_id', 'Passw', 'quizTaken']]
    for index, row in df.iterrows():
        if df['participant_id'].iloc[index] == pid and df['Passw'].iloc[index] == passw:
            return True
    return False


def ifEligible(pid):
    df = pd.read_csv(path / 'participantList.csv')
    df = df[['participant_id', 'Name', 'Gender', 'College', 'City', 'Passw', 'quizTaken']]
    for index, row in df.iterrows():
        if df['participant_id'].iloc[index] == pid and df['quizTaken'].iloc[index] == 0:
            return True
    return False


def update_option_picked(st, pid):
    if ifEligible(pid):
        df = pd.read_csv(path / 'options.csv')
        df = df[['Options', 'Name', 'Option Pick Count']]
        for index, row in df.iterrows():
            if df['Options'].iloc[index] == st:
                df['Option Pick Count'].iloc[index] += 1

        df.to_csv(path / 'options.csv')

        df = pd.read_csv(path / 'participantList.csv')
        df = df[['participant_id', 'Name', 'Gender', 'College', 'City', 'Passw', 'quizTaken']]
        for index, row in df.iterrows():
            if df['participant_id'].iloc[index] == pid:
                df['quizTaken'].iloc[index] = 1

        df.to_csv(path / 'participantList.csv')

        return True
    return False


def show_result():
    df = pd.read_csv(path / 'options.csv')
    df = df[['Options', 'Name', 'Option Pick Count']]
    p_cnt = {}
    for index, row in df.iterrows():
        p_cnt[df['Options'].iloc[index]] = df['Option Pick Count'].iloc[index]
    return p_cnt


def participant_data(name, gender, college, city, passw):
    df = pd.read_csv(path / 'participantList.csv')
    df = df[['participant_id', 'Name', 'Gender', 'College', 'City', 'Passw', 'quizTaken']]
    row, col = df.shape
    if row == 0:
        pid = 10001
        df = pd.DataFrame({"participant_id": [pid],
                           "Name": [name],
                           "Gender": [gender],
                           "College": [college],
                           "City": [city],
                           "Passw": [passw],
                           "quizTaken": [0]}, )
    else:
        pid = df['participant_id'].iloc[-1] + 1
        df1 = pd.DataFrame({"participant_id": [pid],
                            "Name": [name],
                            "Gender": [gender],
                            "College": [college],
                            "City": [city],
                            "Passw": [passw],
                            "quizTaken": [0]}, )

        df = df.append(df1, ignore_index=True)

    df.to_csv(path / 'participantList.csv')

    return pid
