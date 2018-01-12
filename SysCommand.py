import os

abs_res_filepath = os.path.abspath("./scorer/results.txt")
abs_rel_filepath = os.path.abspath("./scorer/SemEval2017-Task3-CQA-QL-dev-subtaskA.xml.subtaskA.relevancy")
abs_script_path = os.path.abspath("./scorer/ev.py")
abs_python_path = "C:\Python\Python36_64\python.exe"

command = abs_python_path + " " + abs_script_path + " " + abs_rel_filepath + " " + abs_res_filepath
os.system(command)