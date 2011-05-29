# Copyright (C) 2010, 2011 Sebastian Thiel (byronimo@gmail.com) and contributors
#
# This module is part of GitDB and is released under
# the New BSD License: http://www.opensource.org/licenses/bsd-license.php
"""Module providing adaptors to maintain backwards compatability"""

class RepoCompatInterface(object):
	"""Interface to install backwards compatability of the new complex repository
	types with the previous, all in one, repository."""
	
	@property
	def bare(self):
		return self.is_bare
		
	def rev_parse(self, *args, **kwargs):
		return self.resolve_object(*args, **kwargs)
		
	@property
	def odb(self):
		"""The odb is now an integrated part of each repository"""
		return self
		
	@property
	def active_branch(self):
		"""The name of the currently active branch.

		:return: Head to the active branch"""
		return self.head.reference
		
	
