#Thought Process

Documentation often reflects the **result** of a series of thoughts used while
you code. But the thoughts put in it to bring the result are effectively lost 
or sometimes kept in bugtrackers/mailing lists. How about having the thought process
you had, while you code, very near to the code itself? This is what this project
intends to do. In short, its like **Twitter for your code!**

Add the thought.process file to each module of your project and keep track of
the ideas you come across while you code. Dont forget to version control it!

Installation:

Add the following line to your .bashrc
    
    alias thoughtprocess='python ~/path/to/thoughtprocess.py'

    
Usage:

    ./thoughtprocess [-f FILE] [-c CATEGORY] [-u USERNAME] [-s STRING] [-lv] [TEXT]
    
TODO:

    * Add an --edit options
    * Use distutils for easy installation
    * Add test cases
