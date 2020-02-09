let store_number = 1;

function locate() {
    if('geolocation' in navigator) {
        console.log('geolocation available');
        navigator.geolocation.getCurrentPosition(async position => {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            const data = {lat,lng};
            const options = {
                method:'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(data)
            };
            console.log("todo send: ", options);

            const response = await fetch('store/', options);
            const json = await response.json();
            console.log(json);
            console.log(json[0]);
            store_number = json[0];
        });

    }
}





async function getProductsInfo(product){
    const options = {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(product)
    };
    console.log('sending: ', options);
    const response = await fetch('products/', options);
    const json = await response.json();
    let products_info = [];
    const d2 = {
        'store_number': store_number,
        'sku':0,
        'name':''
    };
    const option2 = {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(d2),
    };

    for(let i = 0; i < 10; i++){
        if(i === json.length -1){
            break;
        }
        d2.sku = json[i][1];
        d2.name = product;
        option2.body = JSON.stringify(d2);

        const resp = await fetch('price/', option2);
        const output = await resp.json();
        if(output.price == null || output.location == null){
            continue;
        }
        products_info.push(output)
    }

    return products_info
}


locate();

async function testCart(){
    const products = [
        'ice cream',
        'taquitos',
        'lawn chair',
        'corona',
        'milk',
        'ground beef',
        'apples',
        'brocolli',
        'pie',
        'parmesan',
        'sweet and sour chicken',
        'tortillas',
        'mayo',
        'poptarts'
    ];
    for(let product in products){
        await getProductsInfo(product);
    }
}



