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
    df.set_index('proteome', inplace=True)

    print(df['lipoprotein_count'].min())
    print(df['lipoprotein_count'].max())
    print(df['lipoprotein_count'].mean())
    print(df['signalpeptide_count'].median())

    fig = plt.figure(figsize=(30,10))

    ax = fig.add_subplot(111)

    ax2 = ax.twinx()

    width = 0.3

    df.signalpeptide_count.plot(kind='bar', color='red', ax=ax, width=width, position=1)
    df.lipoprotein_count.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

    ax.set_ylabel('Signal Peptide Count', fontsize=16)
    ax2.set_ylabel('Lipoprotein Count', fontsize=16)
    ax.set_xlabel('Sequence', fontsize=16)
    #plt.title('Histogram of ', fontsize=12)
    signal_patch = mpatches.Patch(color='red', label='Signal Peptide')
    lipo_patch = mpatches.Patch(color='blue', label='Lipoprotein')
    plt.legend(handles=[signal_patch,lipo_patch], frameon=False, fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig('out_all.png')

if __name__ == "__main__":
    main()
