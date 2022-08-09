import pandas as pd
from dataframe.read_content import read_content
from dataframe.plot import plot

def main():
  english_films, non_english_films, english_tv_shows, non_english_tv_shows = read_content("dataset.csv")
  plot(english_films, "English Films", "english_films.png")
  plot(non_english_films, "Non English Films", "non_english_films.png")
  plot(english_tv_shows, "English TV Shows", "english_tv_shows.png")
  plot(non_english_tv_shows, "Non English TV Shows", "non_english_tv_shows.png")


if __name__ == '__main__':
  main()