#include <iostream>
#include <fstream>
#include <string>

void readFileCpp(const std::string& filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        std::cerr << "Error: The file could not be opened.\n";
        return;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    if (file.bad()) {
        std::cerr << "Error: An I/O error occurred while reading the file.\n";
    }
    file.close();
}

int main() {
    readFileCpp("randomtext.txt");
    return 0;
}