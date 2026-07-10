# Custom Base64 Encoder

## ⚙️ How It Works (Code Workflow)

Here is the exact step-by-step breakdown of how the logic processes your text:

*   **Step 1:** First it takes the text input from the user.
*   **Step 2:** The variable `decimal` stores ASCII value of all characters of the provided string.
*   **Step 3:** `clean_binary` variable converts those ASCII values into 8 bits binary values and then it gets stored in `binary` list.
*   **Step 4:** All the binary numbers are added one after another and a huge string of binary is made which is stored in `combined_string`.
*   **Step 5:** Now it's checked if the whole string len is divisible by 6 or not if not then add required 0s at the end.
*   **Step 6:** The huge string then separated and each part contains 6 bits of binary numbers.
*   **Step 7:** These 6bits binaries are then converted into decimal numbers and stored in a list named `final_decimal`.
*   **Step 8:** Base64 works by taking groups of 3 bytes (24 bits) and slicing them into 4 chunks of 6 bits each. Every 6-bit chunk maps to a single Base64 character. So if the list `final_decimal` doesn't contain number of elements in multiple of 4 we are adding 404 at the end until it becomes multiple of 4. These 404 will point to "=" sign later.
*   **Step 9:** Now we are accessing the list of base64 characters using each decimal numbers as iterator from `final_decimal` and appending them in the list `encoded_text` and if the number is 404 then we are adding "=" for padding.
*   **Step 10:** Then the whole list is joined together and printed as the encoded base64 text.

---

### 🔤 The Base64 Alphabet Formation
Used string library to create the list. The list is made according to base64 alphabet that is `A-Z`, `a-z`, `0-9`, `+`, `/` . Where index of A is 0.
