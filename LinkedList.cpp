#include <iostream>

class Node{
public:
	int data;
	Node* next;
};

void print(Node* node){
	while(node != NULL){
		std::cout << node->data << " "
		node = node->next;
	}
}

int main(){

	return 0;
}