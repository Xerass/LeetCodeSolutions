#include <stdbool.h>
#include <string.h>
#include <stdio.h>

bool isMatch(char* s, char* p) {
    //dynamic programming approach, we create a table of len(s) x len(p) where we store "matches" per substring
    int m = strlen(s);
    int  n = strlen(p);

    bool SolTable[m+1][n+1];

    //now we would like to instantiate everything to false first
    for(int i = 0; i <= m; i++){
        for(int j = 0; j <= n; j++){
            SolTable[i][j] = false;
        }
    }

    //now we asses per step, first 0,0 which are the empty string matches.
    SolTable[0][0] = true;
    
    //starting from the 2nd valid char we check if that is a *, if so, that means it can match empty string and we fill up , also note that any value before that should also be possible to match.
    for(int j = 2; j <= n; j++){
        if(p[j - 1] == '*'){
            //if value is * that means character before that lambda or not, can be matched, fill up that portion
            SolTable[0][j] = SolTable[0][j-2];
        }
    }

    //starting 1 (first valid char not lambda) attempt to fill up
    for (int i = 1; i <= m; i++){
        for (int j = 1; j <= n; j++){
            //CASE 1: no occurences of previous char, so already valid (up to that point)
            if(p[j - 1] == '*'){
                SolTable[i][j] = SolTable[i][j-2];
            //CASE 2: One or more occurence (checks if prev char is . so any letter or it must match the previous char)
            if (p[j-2] == '.' || p[j-2] == s[i-1]){
                 SolTable[i][j] = SolTable[i][j] || SolTable[i-1][j];
                }
            } else {
                //match for any regular character or .
                if (p[j-1] == '.' || p[j-1] == s[i-1]){
                    SolTable[i][j] = SolTable[i-1][j-1];
                }
                //if not do nothing and let it stay false
            }
            
        }
    }
    //return the final bool
    return SolTable[m][n];
}
