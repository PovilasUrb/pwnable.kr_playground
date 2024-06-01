'''
include <stdio.h>
include <string.h>
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
'''
import struct
Hash = 0x21DD09EC
print(Hash)
# Hash is 568134124
# Since 1 int is equal to 4 bytes and the password is 20 bytes, we need to split it into 5
HashPart = int(Hash/5)
# We get 113626824
lastPart = 568134124 - (4*HashPart)
# missing Hash part is 113626828

# Now we know all the integers so we can convert it back into bytes
password = struct.pack('<i', 113626828) + struct.pack('<i', 113626824) *4

print(password)
# Password is b'\xcc\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06'
# we can run ./col `echo -n -e "\xcc\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06"'
# We can see the flag is "daddy! I just managed to create a hash collision :)"