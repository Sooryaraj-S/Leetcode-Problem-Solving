/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    let binary = n.toString(2);
    let prevIndex = -1;
    let maxDistance = 0;

    for (let i = 0; i < binary.length; i++) {
        if (binary[i] === '1') {
            if (prevIndex !== -1) {
                maxDistance = Math.max(maxDistance, i - prevIndex);
            }
            prevIndex = i;
        }
    }

    return maxDistance;
};