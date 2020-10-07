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

    print(df['count'].max())
    print(df['count'].min())
    print(df['count'].mean())
    print(df['count'].median())

    fig = plt.figure(figsize=(30,10))

    ax = fig.add_subplot(111)

    width = 0.3

    df['count'].plot(kind='bar', color='orange', ax=ax, width=width, position=1)

    ax.set_ylabel('Antibiotic resistance count', fontsize=16)
    ax.set_xlabel('Sequence', fontsize=16)
    #plt.title('Histogram of ', fontsize=12)
    trans_patch = mpatches.Patch(color='orange', label='Antibiotic resistance')
    plt.legend(handles=[trans_patch], frameon=False, fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig('antibiotic_resistance.png')

if __name__ == "__main__":
    main()
