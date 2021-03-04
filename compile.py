import os, shutil
import subprocess
import sys



def pdfLatex( file_name ):
    command = 'pdflatex -synctex=1 -interaction=nonstopmode'
    os.system( command + ' ' + file_name )


def bibTex( file_name ):
    base_name = os.path.splitext( file_name )[0]
    os.system( 'bibtex {}.aux'.format( base_name ) )



if __name__ == '__main__':
    input_file = os.sys.argv[1]
    pdfLatex( input_file )
    bibTex( input_file )
    pdfLatex( input_file )
    pdfLatex( input_file )




subprocess.call("mv %s %s" % ('*.aux', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.lof', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.log', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.lot', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.out', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.xml', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.blg', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.bbl', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('*.toc', 'output_file/'), shell=True)
subprocess.call("mv %s %s" % ('thesis.synctex.gz', 'output_file/'), shell=True)


