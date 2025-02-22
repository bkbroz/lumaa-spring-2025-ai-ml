
# Lumaa AI Challenge

## Get the Datset
Download the IMDB Movies dataset [here](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows), or run the following
```bash
curl -L -o ./imdb.zip https://www.kaggle.com/api/v1/datasets/download/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
unzip ./imdb.zip
``` 

## Download Dependencies
Setup a vritual environment and download the dependencies

```bash
virutalenv env
source env/bin/activate
pip install -r requirements.txt
```

## How to run:
Provide a query to search the dataset with, optionally provide `--results` to modify how many movies are returned

```bash
python recommend.py "Love and romance"
# 1. Gone with the Wind - 1939
# 2. Call Me by Your Name - 2017
# 3. The Apartment - 1960
# 4. Charade - 1963
# 5. Veer-Zaara - 2004

python recommend.py "Love and romance" --results 3
# 1. Gone with the Wind - 1939
# 2. Call Me by Your Name - 2017
# 3. The Apartment - 1960
```

# Salary Expectation:
~ $2000/month (20 hour weeks)