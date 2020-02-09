/**
 * Handles backend API calls for the frontend
 */
let store_number = 1; // Tracks the nearest store.

/**
 * Determines the nearest store to the user through the use of GPS.
 */
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

            const response = await fetch('store/', options);
            const json = await response.json();
            store_number = json[0];
        });

    }
}

/**
 * Returns a list of product information based on the name of a product.
 * @param product String:representing the name of the product.
 * @returns {Promise<[]>} Returns a list of product information.
 */
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
        if(json == null || i === json.length -1){
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

/**
 * Tester function for the backend.
 * @returns {Promise<void>}
 */
async function testCart(){
    const products = [
        'ice cream',
        'taquitos',
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
    let resps = [];
    for(let product in products){
        resp = await getProductsInfo(product);
        if(resp != null){
            resps.push(resp);
        }
    }
    const options = {
        method:'POST',
        'Content-Type':'applications/json',
        'body': JSON.stringify(resps)
    };
    console.log(options);
    const response = await fetch('spf/', options);
    const json = await response.json();
    console.log(json);
}
locate();
