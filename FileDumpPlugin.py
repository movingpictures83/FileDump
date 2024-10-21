import PyPluMA
import PyIO
import os

class FileDumpPlugin:
 def input(self, inputfile):
   self.toRemove = PyIO.readSequential(inputfile)
 def run(self):
     pass
 def output(self, outputfile):
     for myfile in self.toRemove:
        os.system("rm "+PyPluMA.prefix()+"/"+myfile)
