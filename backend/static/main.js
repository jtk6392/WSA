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
            // todo json format tbd do something with the response.
        });

    }
}

async function productPriceLocation(product){
    const options = {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(product)
    };
    console.log('sending: ', options);
    const response = await fetch('product/', options);
    const json = await response.json();
    console.log(json);
    await getPriceLocation(json.sku);

}

async function getPriceLocation(sku){
    const data = {store_number, sku};
    const options = {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify(data)
    };
    console.log('sending: ', options);
    const response = await fetch('price/', options);
    const json = await response.json();
    console.log(json);
}

locate();


