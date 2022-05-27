exports.isCharacterMatch = function(string1, string2) {
//creating str by taking input string running a map to replace all the spaces with nothing, then map again to take each character that matches a character
// to upper case else if not a character just leaving it alone then sorting the output of that map and then joining it back down to a string
let str1 = string1.split('').map(elem => elem.replace(' ', '')).map(elem => elem.match(/[a-zA-Z]/) ? elem.toUpperCase() : elem).sort().join('')
let str2 = string2.split('').map(elem => elem.replace(' ', '')).map(elem => elem.match(/[a-zA-Z]/) ? elem.toUpperCase() : elem).sort().join('')
//just returning the boolen for the comaprative of each string
return str1 === str2
};
