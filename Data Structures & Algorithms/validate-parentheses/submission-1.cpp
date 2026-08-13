class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        for(char c:s){
            if(c=='('||c=='['||c=='{'){
                st.push(c);
            }
            else{
                if(st.empty()){
                    return false;
                }
                char ch=st.top();
                if(ch=='(' && c!=')' || ch=='{' && c!='}' || ch=='[' && c!=']'){
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }
};
