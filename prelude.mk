bin/%: solutions/%.cpp etc/grader.cpp
	g++ $< -o $@ etc/grader.cpp
