#include <string.h>

void reverse(char* s, int left, int right){
    while(left < right){
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left++;
        right--;
    }
}

char* reverseWords(char* s) {


    int n = strlen(s);
    int writer = 0;

    //loop with write read heads, if read sees a char try to make write, write it, else if it finds a space just drop a space
    for(int reader = 0; reader < n; reader++){
        if(s[reader] != ' '){
            //found a non space, must be word, copy it over
            //we want to add a space but if writer is 0 dont else do
            if(writer != 0)  s[writer++] = ' ';

            //do a while loop to cover the entire word
            int word_start = writer;
            while(reader < n && s[reader] != ' '){
                //make writer write that wherever it may be
                s[writer++] = s[reader++];
            }

            //reverse the word
            reverse(s, word_start, writer - 1);
        }
    }

    //at the end writer should be at end pos null terminate it to end the string
    s[writer] = '\0';
    printf("%s", s);

    //reverse the entire sting next
    reverse(s, 0, writer - 1);

    return s;
}
