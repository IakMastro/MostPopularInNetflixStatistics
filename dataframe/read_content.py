import pandas as pd


def parse_movie_data(movie_dataset: pd.DataFrame) -> pd.DataFrame:
  clean_movie_dataset = {
    'rank': movie_dataset['rank'],
    'show_title': movie_dataset['show_title'],
    'hours_viewed_first_28_days': movie_dataset['hours_viewed_first_28_days']
  }

  return pd.DataFrame(clean_movie_dataset)


def parse_tv_show_data(tv_show_dataset: pd.DataFrame) -> pd.DataFrame:
  clean_tv_show_dataset = {
    'rank': tv_show_dataset['rank'],
    'show_title': tv_show_dataset['show_title'],
    'season_title': tv_show_dataset['season_title'],
    'hours_viewed_first_28_days': tv_show_dataset['hours_viewed_first_28_days']
  }

  return pd.DataFrame(clean_tv_show_dataset)


def read_content(path: str):
  dataset: pd.DataFrame = pd.read_csv(path)

  # Fill all NaN to 0 so there will be no problem with the dataset later on
  dataset = dataset.fillna(0)

  # Create seperate arrays for each type of films
  english_films: pd.DataFrame = parse_movie_data(dataset.where(dataset['category'] == "Films (English)").dropna())
  non_english_films: pd.DataFrame = parse_movie_data(dataset.where(dataset['category'] == "Films (Non-English)").dropna())
  english_tv_shows: pd.DataFrame = parse_tv_show_data(dataset.where(dataset['category'] == "TV (English)").dropna())
  non_english_tv_shows: pd.DataFrame = parse_tv_show_data(dataset.where(dataset['category'] == "TV (Non-English)").dropna())

  # Return the newly created datasets in a dictionary
  return english_films, non_english_films, english_tv_shows, non_english_tv_shows
