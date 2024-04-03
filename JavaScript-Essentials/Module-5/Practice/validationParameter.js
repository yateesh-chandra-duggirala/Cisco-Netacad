function getMeanTemp(temperatures) {
    if (!(temperatures instanceof Array)) {
        return "Not an Array";
    }
    let sum = 0;
    for (let i = 0; i < temperatures.length; i++) {
     sum += temperatures[i];
    }
    return sum / temperatures.length;
}
console.log(getMeanTemp(10)); 