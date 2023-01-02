//STL, 자료구조를 활용하자! 모를때는 질문을 한 번 읽어보자!
//cursor 개념이 헷갈려서 처음에 틀렸는데 cursor를 print 해보는 방식으로 디버깅해서 고쳤다.
//이번에는 linked list. 다음번에는 스택으로 도전. left right으로 나누는 방법이 있더라.
#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    list<char> li;
    list<char> :: iterator cursor;
    
    string str, opr;
    char in;
    int i, m = 0;
    
    cin >> str;
    cin >> m;
    
    for (i = 0; i < str.length(); i++){
        li.push_back(str[i]);
    }
    
    cursor = li.end();
    
    for (i = 0; i < m; i++){
        cin >> opr;
        if (opr == "L"){
            //left
            if (cursor != li.begin()){
                cursor--;
            }
        } else if (opr == "D"){
            //right
            if (cursor != li.end()){
                cursor++;
            }
        } else if (opr == "B"){
            //delete left
            if (cursor != li.begin()){
                --cursor;
                cursor = li.erase(cursor);
            }
        } else if (opr == "P"){
            //add to right
            cin >> in;
            li.insert(cursor, in);
        }
    }
    
    for(cursor = li.begin(); cursor != li.end(); ++cursor){
        cout << *cursor;
    }
    
    return 0;
}
