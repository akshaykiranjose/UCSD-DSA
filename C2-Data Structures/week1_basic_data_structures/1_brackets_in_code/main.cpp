#include <iostream>
#include <stack>
#include <string>
#include <fstream>

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main(int argc, char* argv[]) {
    

    if (argc < 2)
    {
        std::cerr<<"Missing argument"<<std::endl;
        return 1;
    }
        
    std::string inFileName = argv[1];  // Assign the first command line argument
    std::ifstream file;   
    file.open(inFileName, std::ios::in); // Open the file

    if (!file)
    {
        std::cerr << "Failed to open file: " << inFileName << std::endl;
        return 1;
    }

    std::string text;
    std::getline(file, text);

    std::stack <Bracket> opening_brackets_stack;
    Bracket* latest_opener;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
            opening_brackets_stack.push(Bracket(next, position));
        }

        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            latest_opener = &opening_brackets_stack.top();
            opening_brackets_stack.pop();

            if (latest_opener->Matchc(next))
            continue;
            else
            {
                std::cout<<position+1;
                return 1;
            }
        }

    }

    // Printing answer, write your code here
    if (opening_brackets_stack.empty())
    {
        std::cout<<"Success";
        return 0;
    }
    else
    {
        latest_opener = &opening_brackets_stack.top();
        std::cout<<latest_opener->position+1;
        return 1;
    }
    
}
