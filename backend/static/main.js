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
            /*
            const response = await fetch(''); // todo interact with backend
            const json = await response.json();
            // todo json format tbd
            */
        });

    }
}
locate();