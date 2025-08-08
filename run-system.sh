./gen-deps.py > deps.mk
cat prelude.mk deps.mk > Makefile
make -j8 -s out/overall.veredict
cat out/overall.veredict
