#!/usr/bin/make
#
all: run

.PHONY: bootstrap buildout run test cleanall
bootstrap:
	virtualenv-2.7 .
	./bin/python bootstrap.py

buildout:
	if ! test -f bin/buildout;then make bootstrap;fi
	bin/buildout -Nvt 5

run:
	if ! test -f bin/instance;then make buildout;fi
	bin/instance fg

test:
	if ! test -f bin/test;then make buildout;fi
	bin/test

cleanall:
	rm -fr bin develop-eggs include lib parts downloads eggs
