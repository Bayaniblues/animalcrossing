import pandas as pd
import urllib.request
import os
import shutil
import random


# Download images process, only accepts one column
def download_images(csv):
    # Check if folder exists
    # Deletes folder if it does
    if os.path.exists('output'):
        shutil.rmtree("output")
    # Rechecks for folder,
    # Make folder
    if not os.path.exists('output'):
        os.mkdir('output')
    # Define dataframe
    df = pd.read_csv(csv)
    #error handling
    #check if df is right shape
    # TODO: error handling to check URLs
    if df.shape[1] != 1:
        return print('error, csv must have 1 column')
    else:
        for i, x in enumerate(list(df.iloc[:,0])):
            try:
                print(f"Getting image{i}", end='\r')
                urllib.request.urlretrieve(x, f"output/{i}.jpg")
            except:
                print(f"Image{i} error", end='\r')
                continue


def animal_crossing_images():
    download_images('animal_crossing.csv')


def jupyter_display(image_path_local):

    from IPython.display import Image
    return Image(filename=image_path_local)


def random_villager():
    # Check if folder exists
    # Deletes folder if it does
    if os.path.exists('random'):
        shutil.rmtree("random")
    # Rechecks for folder,
    # Make folder
    if not os.path.exists('random'):
        os.mkdir('random')

    df = pd.read_csv('animal_crossing.csv')
    x = random.randrange(df.shape[0])

    listToStr = ' '.join(map(str, df.values.tolist()[x]))
    print(listToStr)
    urllib.request.urlretrieve(listToStr, "random/villager.jpg")
    return jupyter_display("random/villager.jpg")
