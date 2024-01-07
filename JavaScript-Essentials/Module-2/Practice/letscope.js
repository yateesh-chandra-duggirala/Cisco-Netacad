
let height = 200;
{
    let weight = 100;
    {
        let info = "This is a piece of Information";
        console.log(height);
        console.log(weight);
        console.log(info);
    }

    console.log(height);
    console.log(weight);
    console.log(info);
}
console.log(height);    // This line will not be executed as the execution stopped at the previous line only.