# Welcome to the Discord Good Morning Script.
This is a python script that you can trigger if you want to send a message to your servers without actually single-handedly going through to each server.

To keep things abstracted and hidden, I have everything linked to a config.json file and all properties are updated there.

## This iteration is if you wanted to run it through chat_gpt so that you don't need a list of variations.
### I didn't use it because it costs money to ping the API & I don't really care that much to do that.



## There is also a .bat file that will execute this script given the following steps:
1. Win + R to access the "Run" Command.
2. "shell:startup"
3. Insert the .bat file & adjust the absolute paths within the script for config.json


Should you run the .bat file from startup, make sure to adjust the line that reads: ' open(r"config.json") ' to read the absolute path to make sure your script can see it!
If you did it right, the adjustment should look like ' open(r"C:/PATH/TO/config.json", 'r')

Thanks,
//Ethan
