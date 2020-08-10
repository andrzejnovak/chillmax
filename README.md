## MadMax Deep Leaning Boost Factors

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
 
