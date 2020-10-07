#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help = "Please input your file")
    args = parser.parse_args()

    input_file = args.f

    f = pd.read_csv(input_file, sep=',', low_memory=False)

    df = pd.DataFrame(f)

    plt.plot(df['percent_identity'], df['clusters'])

    #plt.legend(handles=[trans_patch], frameon=False, fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlabel('Percent Identity', fontsize=16)
    plt.ylabel('Number of clusters', fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig('clustering_faa.png')

if __name__ == "__main__":
    main()
