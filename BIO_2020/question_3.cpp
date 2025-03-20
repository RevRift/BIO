// unsurprisingly the algorithm doesn't work

#include <vector>
#include <iostream>
#include <algorithm>

void increment(std::vector<int>& arr, int max_letter_code, int max_num_of_repeated_letters, int size, int call_number) {
    // maybe for values of p, q and r that allow the initial letter code to be valid
    // this function could fail. make sure to account for this
    // if (call_number == 0 && max_num_of_repeated_letters >= size) {
    //     // initial value of letter_codes is valid
    //     return;
    // }
    auto is_valid = [&](){
        int i = 0, j = 0;
        for (i = 0; i < size; ++i) {
            for (j = i; j < size; ++j)
                if (arr[i] != arr[j]) 
                    break;
            if (j - i + 1 > max_num_of_repeated_letters) 
                return false;
        }
        return true;
    };
    auto plus_one = [&](){
        int i = size - 1;
        arr[i] += 1;
        while (i > 0 && arr[i] > max_letter_code){
            arr[i] = 0;
            arr[i-1] += 1;
            i -= 1;
        }
    };
    do {
        plus_one();
    } while (!is_valid());
}

std::string to_word(const std::vector<int>& letter_codes) {
    std::string word = "";
    for (const char& letter_code : letter_codes)
        word += char(letter_code) + char('A');
    return word;
}

int main() {
    int p, q, r, n;
    std::cin >> p >> q >> r >> n;
    std::vector<int> letter_codes(r, 0);
    for (int i = 0; i < n; ++i) {
        increment(letter_codes, p - 1, q, r, i);
    }
    std::cout << to_word(letter_codes) << '\n';
    return 0;
}