#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>
#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif

class Node;

class Node {
public:
    int key;
    Node *parent;
    std::vector<Node *> children;

    Node() {
      this->parent = NULL;
    }

    void setParent(Node *theParent) {
      parent = theParent;
      parent->children.push_back(this);
    }
};

int HeightIter(Node* ptr)
{
  std::queue<Node*> level_nodes;
  level_nodes.push(ptr);
  int height = 0;
  int num_level_nodes;
  while (!level_nodes.empty())
  {
    num_level_nodes = level_nodes.size();
    for(size_t i=0; i<num_level_nodes; ++i)
    {
      Node* front = level_nodes.front();
      level_nodes.pop();
      for(int i=0; i < front->children.size(); ++i)
        level_nodes.push(front->children[i]);
    }
    height++;
  }
  return height;
}

int HeightRecursive(Node* ptr)
{
  if (ptr->children.empty())
  {
    return 1;
  }
  else
  {
    std::vector<int> subtree_heights;
    for(int i=0; i < ptr->children.size(); ++i)
      subtree_heights.push_back(HeightRecursive(ptr->children[i]));
    int max = 0;
    for(int j: subtree_heights)
    {
      if (j > max)
        max=j;
    }
    return 1 + max;
  }
}

int main_with_large_stack_space(int argc, char *argv[]) {

  
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
    else
    {
        if (file.peek() == std::ifstream::traits_type::eof()) {
        std::cout << "File is empty." << std::endl;
        return 1;
        }
    }
  /**/

  std::ios_base::sync_with_stdio(0);
  int N;
  file >> N;

  std::vector<int> labels;
  
  int node;

  // Read the second line into a string first
  std::string line;
  std::getline(file, line); // To move to the next line
  std::getline(file, line); // Now actually read the second line

  std::istringstream iss(line);
  while (iss >> node) {
      labels.push_back(node);
  }
  /**/

  std::vector<Node> nodes;
  nodes.resize(N);

  int parent_index, root_key;
  for (int child_index = 0; child_index < N; child_index++) {
    parent_index = labels[child_index];
    if (parent_index >= 0)
      nodes[child_index].setParent(&nodes[parent_index]);
    else
      root_key = child_index;
    nodes[child_index].key = child_index;
  }

  /*
  // Replace this code with a faster implementation
  int maxHeight = 0;
  for (int leaf_index = 0; leaf_index < N; leaf_index++) {
    int height = 0;
    for (Node *v = &nodes[leaf_index]; v != NULL; v = v->parent)
      height++;
    maxHeight = std::max(maxHeight, height);
  }
  */

  int maxHeight = HeightIter(&nodes[root_key]);
  //std::cout << root_key << std::endl;
  std::cout << maxHeight << std::endl;
  
  return 0;
}

int main (int argc, char *argv[])
{
#if defined(__unix__) || defined(__APPLE__)
  // Allow larger stack space
  const rlim_t kStackSize = 16 * 1024 * 1024;   // min stack size = 16 MB
  struct rlimit rl;
  int result;

  result = getrlimit(RLIMIT_STACK, &rl);
  if (result == 0)
  {
      if (rl.rlim_cur < kStackSize)
      {
          rl.rlim_cur = kStackSize;
          result = setrlimit(RLIMIT_STACK, &rl);
          if (result != 0)
          {
              std::cerr << "setrlimit returned result = " << result << std::endl;
          }
      }
  }

#endif
  
  return main_with_large_stack_space(argc, argv);
}
