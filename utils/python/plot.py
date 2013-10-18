import matplotlib.pyplot as plt
import numpy as np


def heatmap(df, file_path, xlabel='', ylabel='', cmap=plt.cm.Blues):
    """Plot a heatmap from a pandas dataframe.

    Args:
        df (pandas.DataFrame): data for heatmap plotting
        file_path (str): path to save figure (png, pdf, etc.)
        xlabel (str): x-axis label
        ylabel (str): y-axis label
        cmap (cm): color scheme for heatmap

    Code from:
    http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor
    """
    df = df.fillna(0)  # fills missing values with 0's

    # make heatmap
    fig, ax = plt.subplots()
    hmap = ax.pcolor(df, cmap=cmap, alpha=0.8)

    fig = plt.gcf()
    fig.set_size_inches(8,11)

    # turn off the frame
    ax.set_frame_on(False)

    # put the major ticks at the middle of each cell
    ax.set_yticks(np.arange(df.shape[0])+0.5, minor=False)
    ax.set_xticks(np.arange(df.shape[1])+0.5, minor=False)

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    # Set the labels
    labels = df.index
    ax.set_xticklabels(labels, minor=False)
    ax.set_yticklabels(df.index, minor=False)

    # rotate the
    plt.xticks(rotation=90)

    ax.grid(False)

    # Turn off all the ticks
    ax = plt.gca()

    for t in ax.xaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False

    # handle labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()

    # save figure
    plt.savefig(file_path)


def barplot(df, file_path, title='', xlabel='', ylabel='', stacked=False):
    df.plot(kind='bar', stacked=stacked)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(file_path)
    plt.clf()  # clear figure


def histogram(df, file_path, title='', xlabel='', ylabel=''):
    df.hist(bins=range(0, 300, 5), log=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    #plt.semilogy()
    plt.savefig(file_path)
    plt.clf()  # clear figure


def line(data, file_path,
         title='',
         xlabel='',
         ylabel='',
         logx=False,
         logy=False,
         vlines=[]):
    # plot data
    data.plot(kind='line')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # log scale if neccessary
    if logx:
        plt.xscale('log')
    if logy:
        plt.yscale('log')

    # plot vertical lines
    ymin, ymax = plt.ylim()  # get plotting range of y-axis
    for l in vlines:
        plt.vlines(l, ymin=ymin,
                   ymax=ymax,
                   color='red')

    plt.tight_layout()
    plt.savefig(file_path)
    plt.clf()  # clear figure


def scatter(x, y,
            file_path,
            colors='blue',
            title='',
            xlabel='',
            ylabel=''):
    plt.scatter(x, y, c=colors)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(file_path)
    plt.clf()  # clear figure
