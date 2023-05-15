/*
    Write a function to find out whether the binary representation of a number is palindrome or not.

    eg -
    > binaryPal(5)
    > true

    > binaryPal(10)
    > false
*/
/**
 * @param {number} num
 * @return {string}
 */
function toBinary(num) {
    return num.toString(2);
}
/**
 * @param {string} num
 * @returns {boolean}
 */
function checkPallindrome(num) {
    var i = 0, j = num.length - 1;
    while (i < j) {
        if (num[i] != num[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}
/**
 * IIFE main
 * @returns {void}
 */
(function main() {
    // inputs are placed in this array
    var inputs = [5, 10];
    // for each input respective output is produced
    inputs.forEach(function (value) {
        console.log(checkPallindrome(toBinary(value)));
    });
})();
