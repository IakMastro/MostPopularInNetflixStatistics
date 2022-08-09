import pandas as pd
from matplotlib import pyplot as plt

def plot(dataset: pd.DataFrame, label: str, file_name: str):
  print(dataset)
  plt.plot(dataset['rank'], dataset['hours_viewed_first_28_days'], label=label)
  plt.title("Most Popular In Netflix - " + label)
  plt.xlabel("Rank")
  plt.ylabel("Number of views")
  plt.savefig(file_name)
  plt.legend()
  plt.show()
