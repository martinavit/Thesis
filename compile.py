import os, shutil
import subprocess



os.system("pdflatex thesis.tex")

subprocess.call("mv %s %s" % ('*.aux', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.lof', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.log', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.lot', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.out', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.xml', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.toc', 'output_file/'), shell=True)
