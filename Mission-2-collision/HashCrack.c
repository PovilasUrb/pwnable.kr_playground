/*
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
*/
#include <stdio.h>  // For printf
#include <stdlib.h> // For malloc and free

char* reverseOperation(int res) {
    // Allocate memory for 5 integers, assuming this was the original structure
    int* ip = malloc(5 * sizeof(int));
    
    // Dummy operation: let's just distribute `res` evenly for demonstration
    // This is purely illustrative and doesn't "reverse" the original operation meaningfully
    for (int i = 0; i < 5; i++) {
        ip[i] = res / 5;
    }
    
    // Casting back to char* for demonstration, akin to the original question's cast
    char* p = (char*)ip;
    
    // WARNING: This is just for demonstration and doesn't reconstruct original data
    return p;
}

unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}
int main() {
    // Example usage
    int res = 0x21DD09EC; // Example result
    char* p = reverseOperation(res);
    printf("%lu\n", check_password(p));

    // Remember to free the allocated memory to avoid memory leaks
    int* ip = (int*)p; // Cast it back to int* to properly deal with it
    for (int i = 0; i < 5; i++) {
        printf("%d ", ip[i]); // Print the integers to see the distribution
        
    }
    free(ip); // Free the allocated memory
    
    return 0;
}

