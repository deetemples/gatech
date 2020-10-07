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
    df.set_index('File', inplace=True)

    print(df['crispr'].max())
    print(df['crispr'].min())
    print(df['crispr'].mean())
    print(df['crispr'].median())


    fig = plt.figure(figsize=(30,10))

    ax = fig.add_subplot(111)

    width = 0.3

    df.crispr.plot(kind='bar', color='purple', ax=ax, width=width, position=1)

    ax.set_ylabel('CRISPR Count', fontsize=16)
    ax.set_xlabel('Sequence', fontsize=16)
    #plt.title('Histogram of ', fontsize=12)
    trans_patch = mpatches.Patch(color='purple', label='CRISPR')
    plt.legend(handles=[trans_patch], frameon=False, fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig('crispr.png')

if __name__ == "__main__":
    main()
