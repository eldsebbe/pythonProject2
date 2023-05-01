import os
import pandas as pd


CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def biology_combine():  #Combines data from all biology.txt files into one

    biology_mega_path = CURR_DIR_PATH + "/data/biology_00.txt"
    biology_mega = pd.read_csv(biology_mega_path)
    for i in range(1, 31):
        biology_mega_path = CURR_DIR_PATH + "/data/biology_0" + str(i) + ".txt"
        biology_temp = pd.read_csv(biology_mega_path)
        biology_mega = biology_mega.append(biology_temp)
    biology_mega_path = CURR_DIR_PATH + "/data/biology_data.csv"

    biology_mega.to_csv(biology_mega_path, index=False)


def herbology_combine():    #Combines data from all herbology.txt files into one

    herbology_mega_path = CURR_DIR_PATH + "/data/herbology_00.csv"
    herbology_mega = pd.read_csv(herbology_mega_path)
    for i in range(1, 31):
        herbology_mega_path = CURR_DIR_PATH + "/data/herbology_0" + str(i) + ".csv"
        herbology_temp = pd.read_csv(herbology_mega_path)
        herbology_mega = herbology_mega.append(herbology_temp)
    herbology_mega_path = CURR_DIR_PATH + "/data/herbology_data.csv"

    herbology_mega.to_csv(herbology_mega_path, index=False)


def math_combine(): #Combines data from all math.txt files into one

    math_mega_path = CURR_DIR_PATH + "/data/math_00.csv"
    math_mega = pd.read_csv(math_mega_path)
    for i in range(1, 31):
        math_mega_path = CURR_DIR_PATH + "/data/math_0" + str(i) + ".csv"
        math_temp = pd.read_csv(math_mega_path)
        math_mega = math_mega.append(math_temp)
    math_mega_path = CURR_DIR_PATH + "/data/math_data.csv"

    math_mega.to_csv(math_mega_path, index=False)


def pe_combine():   #Combines data from all pe.txt files into one

    pe_mega_path = CURR_DIR_PATH + "/data/pe_00.txt"
    pe_mega = pd.read_csv(pe_mega_path)
    for i in range(1, 31):
        pe_mega_path = CURR_DIR_PATH + "/data/pe_0" + str(i) + ".txt"
        pe_temp = pd.read_csv(pe_mega_path)
        pe_mega = pe_mega.append(pe_temp)
    pe_mega_path = CURR_DIR_PATH + "/data/pe_data.csv"

    pe_mega.to_csv(pe_mega_path, index=False)


def physics_combine():  #Combines data from all physics.txt files into one

    physics_mega_path = CURR_DIR_PATH + "/data/physics_00.csv"
    physics_mega = pd.read_csv(physics_mega_path)
    for i in range(1, 31):
        physics_mega_path = CURR_DIR_PATH + "/data/physics_0" + str(i) + ".csv"
        physics_temp = pd.read_csv(physics_mega_path)
        physics_mega = physics_mega.append(physics_temp)

    physics_mega_path = CURR_DIR_PATH + "/data/physics_data.csv"

    physics_mega.to_csv(physics_mega_path, index=False)


def combine_names(dirlink): #combines first name and surname into one name
    df = pd.read_csv(dirlink)
    df["name"] = df[["firstname", "surname"]].apply(" ".join, axis=1)
    df = df.drop(["firstname", "surname"], axis=1)
    df.to_csv(dirlink, index=False)


def is_late(dirlink):   #changes attendance to late and calkulates the minutes late if lesson =60 min
    df = pd.read_csv(dirlink)
    df["late"] = df["attendance"]

    for i in range(0, 182):
        if df.loc[i, "late"] == 60:
            df.loc[i, "late"] = 0

        else:
            df.loc[i, "late"] = 60 - df.loc[i, "late"]


    df = df.drop(["attendance"], axis=1)
    df.to_csv(dirlink, index=False)
