## MadMax Deep Leaning Boost Factors

## Package management and github
It's advisable to keep all (python) packages in a virtual environment managed by conda

To install conda you can run the following and then follow the instructions.
When asked to add stuff to .bashrc you should say yes
```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

In python most real packages are published on pypi, so one can usually just run 
something like `pip install numpy`, however, our package is private so we don't
want to publish it, but we can still use the `pip` installation.

To do this you first need to clone it from github.
```
git clone git@github.com:andrzejnovak/chillmax.git
```

and then go into the package and install it as editable 
 - `.` means install this folder
 - `-e` means install as editable - meaning changes to the codebase will have an immediate effect

so:
 ```
cd chillmax
pip install -e .
 ```

Then you should be able to `import chillmax` like any other package like numpy

### Use
#### Installation
- Repo is packaged with some scripts being available as a regular package - notably simulation
- To install (having a conda environment is recommended, ping me if you don't):
  - `-e` means editable, so your package will always run what's currently in the directory
```
pip install -e . 
```

#### Workflow
- We should externalize useful scripts into the package, while keeping the development 
in jupyter notebooks
- Ideally code should be validated by tests
  - Examples can be found in `test/`
  - `test/test_base.py::test_boost` shows how to call the boost factor prediciton
  from the original `Analytical1D.py` code (absorbed)
  - CI is set up, the test will run on github, whenever new stuff is pushed. I don't think 
  we need to do this very strictly, but as a rule, no breaking changes should be
  introduced
 
