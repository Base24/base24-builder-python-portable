#!/usr/bin/env python3
import os
import sys
import shutil
import asyncio

# clone base24-builder-python-portable
async def git_clone():
	proc_env = os.environ.copy()
	proc_env["GIT_TERMINAL_PROMPT"] = "0"
	path = "base24-python-portable"
	git_proc = await asyncio.create_subprocess_exec(
		"git", "clone", "https://github.com/Base24/base24-python-portable", path, stderr=asyncio.subprocess.PIPE, env=proc_env
	)
	_stdout, stderr = await git_proc.communicate()

	if git_proc.returncode != 0:
		# remove created directory if it's empty
		try:
			os.rmdir(path)
		except OSError:
			pass

# copy base24_builder/* and base24
def copytree(src, dst, symlinks=False, ignore=None):
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		if os.path.isdir(s):
			shutil.copytree(s, d, symlinks, ignore)
		else:
			shutil.copy2(s, d)

def copy_dropin():
	copytree(os.getcwd() + os.sep + "base24-python-portable" + os.sep + "base24_builder", os.getcwd() + os.sep + "base24_builder")
	shutil.copy2(os.getcwd() + os.sep + "base24-python-portable" + os.sep + "base24.py", os.getcwd() + os.sep + "base24.py")


git_clone()
copy_dropin()
