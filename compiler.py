import sys

class Tree:
	def __init__(self):
		self.children = []
		self.rootnode = None


def compile(*source_files):
	pass

def add_to_decl_trie(trie, declaration):
	''' Adds the given function declaration into the given declaration trie.'''
	pass

def is_comment(line):
	return line.strip.startswith("#")

	

def main():
     """Runs program and handles command line options"""
    if len(sys.argv) <= 2:
		print "Error: Specify at least one source file to compile."
		print "Usage: ctalk <sourcef file 1> <source file 2>..."

	compile(sys.argv[1:])

   
if __name__ == '__main__':
	main()

