exec = Test.exe
sources = $(wildcard *.cpp)
objects = $(sources:.cpp=.o)
flags = -g

$(exec): $(objects)
    g++ $(objects) $(flags) -o $(exec)

%.o: %.cpp ../include/%.hpp
    g++ -c $(flags) $< -o $@

clean:
    -rm *.exe
    -rm *.o