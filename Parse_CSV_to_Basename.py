import pandas as pd
import ntpath


in_csv = r'C:\Users\19033\Desktop\RA Lisa\JabRef\Export-12-12-2.csv'  # full path to the CSV containing information
                                                                      # that was exported from your JabRef or Zotero.
                                                                      
column = r'Path'  # Change this to reflect the name of the column containing the path to the file on your computer.

df = pd.read_csv(in_csv, encoding='latin1')

new_items = []

for item in df[column]:
    try:
        item_v = str(ntpath.basename(item))
        new_items.append(item_v)
    except TypeError:
        new_items.append('NA')

df.loc[:, column] = new_items

df.to_csv('path/to/new-csv.csv')  # Change this to the path and name of your new CSV. See above to reference format.