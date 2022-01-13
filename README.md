# ObjectDetactionTools
 Tools I made for making the dark net object detaction traning process smoother

## listGen.py
- Automaticly generate train.txt and test.txt file to the data folder under darknet
- Can define file path to replace the default address of Darknet in command line
- How to use it? 'listGen.py [test/train]'
  - train and test option will generate a train.txt file and a test.txt file respectively
  - '-r n-m': set the range of the folder you want to use, from number n to m
  - '-p path': set Darknet path if not wish to use the default address

## lableCount.py
- Count the amount of each labels in the data set
- How to use it? 'labelCount.py [-p filePath]'

## indexChanger.py
- If added label between two existed labels, you can use this tool to shift the label index of all the effected data
- How to use it? 'indexChanger.py index interval [-p Path] [-r] [-re]'
- index: The target index, the target index will be shifted
- interval: Define the shift amount, new index = index + intervel
- '-p path': Define file path
- '-r': reverse the shift, new index = index - intervel
- '-re': Repeat the action, all the indexes after the target (target index included) will be shifted
- '-h': help page for how to use this tool
