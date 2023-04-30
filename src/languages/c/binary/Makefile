exec = Test.exe
sources = $(wildcard *.c)
objects = $(sources:.c=.o)
flags = -g

$(exec): $(objects)
	gcc $(objects) $(flags) -o $(exec)

%.o: %.c ../include/%.h
	gcc -c $(flags) $< -o $@

clean:
	-rm *.exe
	-rm *.o