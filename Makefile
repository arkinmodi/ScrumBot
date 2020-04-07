PY = python3
PT = pytest
PYFLAGS = --cov-report html --cov=src/ 
DOXY = doxygen
DOXYCFG = doxConfig

RMDIR = rm -rf

.PHONY: run test doc clean

run:
	$(PY) src/scrumbot.py

test:
	$(PT) $(PYFLAGS) src/test.py

doc:
	$(DOXY) $(DOXYCFG)
	cd latex && $(MAKE)

clean:
	@- $(RMDIR) html
	@- $(RMDIR) htmlcov
	@- $(RMDIR) latex
