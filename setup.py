import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="test-package",
	version="0.0.1",
	author="sachin",
	author_email="reachsachinquick@gmail.com",
	packages=["package2"],
	description="A sample test package",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/sac1103/new-folder-2-.git",
	license='MIT',
	python_requires='>=3.8',
	install_requires=[]
)
