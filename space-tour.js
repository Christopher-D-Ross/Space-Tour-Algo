// Here are the travel costs for the weeks we are interested in:
 
// Week 1:  $ 4,000
// Week 2:  $21,000
// Week 3:  $ 3,000
// Week 4:  $11,000
// Week 5:  $ 2,500
// Week 6:  $ 7,000
// Week 7:  $25,000
// Week 8:  $18,000
// Week 9:  $25,500
// Week 10: $12,000
// Week 11: $ 1,500
// Week 12: $18,000

// This function takes in an array of prices/integers along with two other optional inputs that represent the travelers departure and return week.

// let firstTwelveWeeks = [4000, 21000, 3000, 11000, 2500, 7000, 25000, 18000, 24000, 12000, 1500, 19000];

// function priceDifference(arr, numGo, numLv) {
//     let maxPrice = Math.max(...arr);
//     let minPrice = Math.min(...arr);
//     let maxPos = arr.indexOf(maxPrice);
//     let minPos = arr.indexOf(minPrice);
//     let departPrice = firstTwelveWeeks[numGo - 1];
//     let returnPrice = firstTwelveWeeks[numLv - 1];
//     console.log("Details for the maximum difference between travel for weekly prices provided are as follows:");
//     console.log(`The most expensive week is week ${maxPos + 1} with a travel cost of $${maxPrice}.`);
//     console.log(`The least expensive week is week ${minPos + 1} with a travel cost of $${minPrice}.`);
//     console.log(`The difference between the prices having had traveled during these two weeks is $${maxPrice - minPrice}.`);
//     console.log(`Based on your desired departure and return dates the total cost of your trip will be $${departPrice + returnPrice}.`);
//     if(departPrice - returnPrice < 0) {
//         let difference = (departPrice - returnPrice) * -1;
//         console.log(`The difference between your departure price and return price is $${difference}.`);
//     } else {
//         console.log(`The difference between your departure price and return price is $${departPrice - returnPrice}.`);
//     }
// }

// priceDifference(firstTwelveWeeks, 1, 2);

let firstTwelveWeeks = [4000, 21000, 3000, 11000, 2500, 7000, 25000, 18000, 24000, 12000, 1500, 19000];

function priceDifference(arr, numGo, numLv) {
    let maxPrice = Math.max(...arr);
    let minPrice = Math.min(...arr);
    let maxPos = arr.indexOf(maxPrice);
    let minPos = arr.indexOf(minPrice);
    let departPrice = arr[numGo - 1];
    let returnPrice = arr[numLv - 1];
    console.log("Details for the maximum difference between travel for weekly prices provided are as follows:");
    console.log(`The most expensive week is week ${maxPos + 1} with a travel cost of $${maxPrice}.`);
    console.log(`The least expensive week is week ${minPos + 1} with a travel cost of $${minPrice}.`);
    console.log(`The difference between the prices having had traveled during these two weeks is $${maxPrice - minPrice}.\n`);
    if(departPrice - returnPrice < 0 && numGo <= numLv) {
        let difference = (departPrice - returnPrice) * -1;
        console.log(`The difference between your departure price and return price is $${difference}.`);
        console.log(`Based on your desired departure and return dates the total cost of your trip will be $${departPrice + returnPrice}.\n`);
    } else if(departPrice - returnPrice > 0 && numGo <= numLv) {
        console.log(`The difference between your departure price and return price is $${departPrice - returnPrice}.`);
        console.log(`Based on your desired departure and return dates the total cost of your trip will be $${departPrice + returnPrice}.\n`);
    } else {
        console.log("You cannot travel back in time. Choose correct travel times.\n")
    }
    let configArr = arr.slice(numGo);
    let returnDifferencesNeg = configArr.map((price) => departPrice - price);
    let returnDifferencesPos = returnDifferencesNeg.map((diff) => {
        if(diff < 0) {
            return diff * -1;
        } else {
            return diff * 1
        }
    });
    let minDiff = Math.min(...returnDifferencesPos);
    let maxDiff = Math.max(...returnDifferencesPos);
    let minDiffIndex = returnDifferencesPos.indexOf(minDiff) + numGo + 1;
    let maxDiffIndex = returnDifferencesPos.indexOf(maxDiff) + numGo + 1;
    console.log(`Information regarding your return options based on your week ${numGo} departure choice:\n`)
    console.log(`The largest difference in cost you can incur when returning is the result of coming back to earth in week ${maxDiffIndex}.`);
    console.log(`The smallest difference in cost you can incur when returning is the result of coming back to earth in week ${minDiffIndex}.`);
}
priceDifference(firstTwelveWeeks, 2, 6);