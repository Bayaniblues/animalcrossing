# Animal Crossing library
I don't have a Nintendo Switch so this is the next best thing.

Animal crossing villagers for computer vision projects.

And basic utilities for computer vision.

![animalcrossing](./random/villager.jpg)
[Image source animal crossing world](https://animalcrossingworld.com/2020/02/250-high-resolution-animal-crossing-new-horizons-villager-special-character-renders/)

[Nintendo Germany, NintenDaan](https://twitter.com/NintenDaan)
## Quickstart

    import animalcrossing as ac
    
    ac.random_villager()
    
## Utilities
download_images method to pull images from the internet with the pandas dataframe

The jupyter_display method displays images in jupyter notebook

    import pandas as pd
    urls = ['https://i.ytimg.com/vi/XOXckrf_RoQ/maxresdefault.jpg', 
            'https://i.insider.com/56688a26dd0895106a8b478b?width=1762.jpg']
    df = pd.DataFrame(urls, columns=['Name'])
    
    # export to csv, make sure index is false
    df.to_csv('walle.csv', index=False)
    ac.download_images('walle.csv')

    ac.jupyter_display('output/0.jpg')
    

## Get all images
Grabs about 250 images but will take a long time to scrape.

    ac.animal_crossing_images()

## License
The technology is registered under MIT but please respect nintendo's trademark

ANIMAL CROSSING is a trademark of Nintendo of America Inc.