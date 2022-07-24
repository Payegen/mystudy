function add(a,...arg){
    const aset = new Set(a);
    arg.forEach(e=>{
        aset.add(e)
    })
    console.log(Array.from(aset));
}
add([0],1,2,3,4)