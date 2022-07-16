function Euclidean (hash){
    let num = 0;
    for (let index = 0; index < 255; index++) {
        num = (this.hash[index] - hash[index]) + num;
    }
    return Math.abs(num);
}

function euclidean1 (hash1,hash2){
    let num = 0;
    for (let index = 0; index < 2; index++) {
        num = (hash2[index] - hash1[index]) + num;
    }
    return Math.abs(num);
}




let hash1 = [
20,
30
]
let hash2 = [
10,
6660
]
let c = euclidean1 (hash1,hash2);
console.log(c);