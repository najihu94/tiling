import os
from PIL import Image

"""
Go to the output folders generated by HoverNet inference prediction and copy the file of interest to the
previous directory in the tree structure changing the name of the file in the desired format.
The folder must contain only sub-folders coming from HoVerNet outputs.
"""
imageofinterest = 'overlay.png'  # can be overlay.png or instances.png in the case. Needs to remove result from directory to generate other one!

Outputdir = '/home/lsancere/These/CMMC/Cheops1_Mount_Projects/Data_General/Predictions/IHC_HE_ScieboData1/HE/Inputs_sample_008_overlappingVer_tiles_hovernet_inference/Outputs'

for root, dirs, files in os.walk(Outputdir):
    newname = root + '.png'
    if files != [] and os.path.exists(newname) == False and root != Outputdir:
        imagepath = root + '/' + imageofinterest
        image = Image.open(imagepath)
        image.save(newname)
        print('image saved :', newname)
