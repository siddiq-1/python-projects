import pywhatkit as pw

string='''If you have gained enough knowledge about the Python programming language and want to get selected in any company at a good salary, this video is for you.'''

pw.text_to_handwriting(string,"hand.png",[225,149,38])
print("End")