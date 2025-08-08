#include <iostream>
#include "aplusb.h"
int main() {
	int a, b;
	std::cin >> a >> b;
	int result = aplusb(a, b);
	std::cout << result << "\n";
}
