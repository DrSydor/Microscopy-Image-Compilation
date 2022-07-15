"""
This script will create compilations of the CLEM microscope images. A separate
pdf file will be generated for each of the treatment conditions. The image
inputs are direct RGB .tif exports from Volocity and assumes that the green
channel image will have the filename "T00001C02Z001.tif" and the red channel
image will have the filename "T00001C01Z001.tif".
"""

from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

conditions = ['1-Post Fix and Os',
              '2-Post TUK',
              '3-Post EtOH',
              '4-Pre Curing',
              '5-Post Curing',
              '6-Month Later']

condition_names = ['Post Fixation and OsO4',
              'Post TUK Multicolor Solution',
              'Post EtOH Dehydration',
              'Pre-resin curing',
              'Post resin curing',
              'In-block, 1 month later']

treatments = ['Tanida et al. Method',
              '+ 2% Tannic Acid',
              '+ 0.05% Malachite Green',
              '+ 0.2% Ruthenium Red']

def plot(treatment, condition):

    treatment += 1

    green_img = io.imread('D:/Correlative/Light Microscopy/20220615- CLEM Test Images/' + str(treatment) + '-' + conditions[condition] + '/T00001C02Z001.tif')
    red_img = io.imread('D:/Correlative/Light Microscopy/20220615- CLEM Test Images/' + str(treatment) + '-' + conditions[condition] + '/T00001C01Z001.tif')

    fig = Figure(figsize=(4,3), dpi=600)
    fig.suptitle(f'{condition_names[condition]}', fontsize = 18)
    canvas = FigureCanvasAgg(fig)

    axs = fig.add_gridspec(ncols=2, nrows=1)
    ax1 = fig.add_subplot(axs[0,0])
    ax1.imshow(green_img)
    ax1.set_title('mWasabi-Rab10', fontsize=14)
    ax1.axis('off')
    ax2 = fig.add_subplot(axs[0,1])
    ax2.imshow(red_img)
    ax2.set_title('mito-mCherry2', fontsize=14)
    ax2.axis('off')

    fig.tight_layout()
    canvas.draw()
    buf = canvas.buffer_rgba()
    X = np.asarray(buf)
    return X

def master_plot(treatment):

    fig = plt.figure(figsize = (4,5), dpi = 600)
    fig.suptitle(f'In-resin fluorescence tests:\n {treatments[treatment]}', fontsize=12)
    axs = fig.subplot_mosaic([['TopLeft', 'TopRight'],['MidLeft', 'MidRight'], ['BottomLeft', 'BottomRight']])

    axs['TopLeft'].imshow(plot(treatment, 0))
    axs['TopLeft'].axis('off')

    axs['TopRight'].imshow(plot(treatment, 1))
    axs['TopRight'].axis('off')

    axs['MidLeft'].imshow(plot(treatment, 2))
    axs['MidLeft'].axis('off')

    axs['MidRight'].imshow(plot(treatment, 3))
    axs['MidRight'].axis('off')

    axs['BottomLeft'].imshow(plot(treatment, 4))
    axs['BottomLeft'].axis('off')

    axs['BottomRight'].imshow(plot(treatment, 5))
    axs['BottomRight'].axis('off')

    fig.tight_layout()

    name = 'CLEM test- ' + treatments[treatment] + '.pdf'
    plt.savefig(name)

for n in range(4):
    master_plot(n)
