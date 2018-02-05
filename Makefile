all: de en

de:
	$(MAKE) -C $@

en:
	$(MAKE) -C $@

.PHONY: all de en
