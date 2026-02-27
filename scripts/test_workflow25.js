async function getData(){
    const url = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Tyrannosaurus_rex_Sue_at_FMNH.jpg/440px-Tyrannosaurus_rex_Sue_at_FMNH.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Mosasaurus_beaugei_34.JPG/440px-Mosasaurus_beaugei_34.JPG"
    ]
    return url;
   }
   
   getData().then((url) => {
    console.log(url);
   });