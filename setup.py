import setuptools

with open("README.md",'r')as fh:
	long_description =fh.read()

setuptools.setup(
	name="TWT",
	version="0.0.1",
	author="Hunter-Ou",
	author_email="oy199603@qq.com",
	description="Dedicated in the SAR",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/UCAS-BigBird/Tkinter",
	packages=setuptools.find_packages(),
	classifiers=[
				"Programming Language::Python::3",
				"License::OSI Approved::MIT License",
				"Operating System::OS Independent",
				],
	python_requires='>=3.6',
)